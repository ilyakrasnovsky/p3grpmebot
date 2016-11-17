'''
module : behavior

has common/helpful bot behavior routines

'''

import groupy
from bot.models import groupMeBot
from django.conf import settings
from cleverbot import Cleverbot

#import requests

class Behavior():
    def __init__(self):
        self.cb = Cleverbot()

    #get information about myself
    def meMyselfAndI(self):
        return groupy.User.get()

    #broken on groupme API, DO NOT USE
    '''
    def changeMyName(self, newname, groupName):
        payload = {"token" : settings.GROUPMEBOT_GROUPME_SECRET_KEY,
               "membership" : {
                    "nickname" : newname
                            }
            }
        response = requests.post("https://api.groupme.com/v3/groups/" + str(self.getGroupID(groupName)) "/memberships/update", params=payload)
        print ("status code : " + str(response.status_code))
    '''

    #get an existing bot by name (string)
    #returns Bot instance (groupy API) if found,
    #None if not
    def getBot(self, name):
        modelbot = groupMeBot.botmanager.getBotByName(name)
        if (modelbot is not None):
            for mybot in groupy.Bot.list():
                if (mybot.name == name):
                    return mybot
        return None

    #make a bot to haunt victimName string) in groupName (string)
    #with avatar_url (groupMe URL as string) and callback_url
    #returns True if successful, False if not
    def botAssimilate(self, victimName, groupname, avatar_url, callback_url):
        if (self.getVictimFromGroup(victimName, groupname) is not None):
            if (self.addBot(name=victimName + " ",
            				groupname=groupname,
            				avatar_url=avatar_url,
            				callback_url=callback_url,
            				victimID=self.getVictimFromGroup(victimName=victimName, groupname=groupname).user_id)):
                return True
        return False

    def addBot(self, name, groupname, victimID, avatar_url, callback_url):
        if (groupMeBot.botmanager.getBotByName(name) is None):
            try:
                newbot = groupy.Bot.create(name=name, 
                                  		   group=self.getGroupByName(groupname),
                                  		   avatar_url=avatar_url,
                                  		   callback_url=callback_url)
                if (groupMeBot.botmanager.addBot(name=newbot.name,
                                                 botID=newbot.bot_id,
                                                 victimID=victimID,
                                                 groupname=groupname,
                                                 avatar_url=newbot.avatar_url,
                                                 callback_url=newbot.callback_url) == False):
                    newbot.destroy()
                    return False
                return True
            except groupy.api.errors.ApiError:
                return False
        return False

    #destroy the bot given by botname (string), if it exists
    def destroyBot(self, botname):
        bot_to_destroy = self.getBot(botname)
        if (bot_to_destroy is not None):
            groupMeBot.botmanager.removeBotByName(botname)
            bot_to_destroy.destroy()
            return True
        return False

    #get an existing group by name (string)
    #returns Group instance (groupy API) if found,
    #None if not
    def getGroupByName(self, groupname):
        for group in groupy.Group.list(): 
            if(group.name == groupname):
                return group
        return None

    def getGroupByID(self, groupID):
        for group in groupy.Group.list(): 
            if(group.group_id == groupID):
                return group
        return None

    def getVictimByID(self, victimID):
        for mem in groupy.Member.list():
            #print (mem.identification()['nickname'] + " : " + str(mem.identification()['user_id']) + ", " + str(mem.identification()['guid']))
            try:
                if (mem.identification()['user_id'] == victimID):
                    return mem
            except ValueError:
                print ("Fail")
                return None
        return None

    #Finds a victim whose name is victimName(string)
    #in the groupme group given by groupName. returns
    #Member instance (groupy API) if found, None if not
    def getVictimFromGroup(self, victimName, groupname):
        group = self.getGroupByName(groupname)
        if (group is not None):
            for mem in group.members():
                if (mem.identification()['nickname'] == victimName):
                    return mem
        return None

    #bot updates its name
    def botAdaptToNameChange(self, newVictimName, oldVictimName):
        bot = self.getBot(oldVictimName + " ")
        if (bot is not None):
            avatar_url = bot.avatar_url
            callback_url = bot.callback_url
            group = self.getGroupByID(bot.group_id)
            if (group is not None and self.getVictimFromGroup(newVictimName, group.name) is not None):
                groupname = group.name
                #bot.post("I take my leave, and pass the torch.")
                self.destroyBot(oldVictimName + " ")
                success = self.botAssimilate(newVictimName,
                                    groupname,
                                    avatar_url,
                                    callback_url)
                if (success):
                    newbot = self.getBot(newVictimName + " ")
                    if (newbot is not None):
                        #newbot.post("I have picked up the torch. HueHueHue...")
                        return True
        return False

    def botAdaptToAvatarChange(self, victimName, newVictimAvatar):
        bot = self.getBot(victimName + " ")
        if (bot is not None):
            callback_url = bot.callback_url
            groupname = self.getGroupByID(bot.group_id).name
            if (groupname is not None):
                #bot.post("I take my leave, and pass the torch.")
                self.destroyBot(victimName + " ")
                success = self.botAssimilate(victimName,
                                    groupname,
                                    newVictimAvatar,
                                    callback_url)
                if (success):
                    newbot = self.getBot(victimName + " ")
                    if (newbot is not None):
                        #newbot.post("I have picked up the torch. HueHueHue...")
                        return True
        return False

    def botBehave(self, name, message):
        bot = self.getBot(name)
        if (bot is not None):
            response = self.cb.ask(message)
            if (response is not None):
                bot.post(response)
                return True
        return False

    def getBotByVictimID(self, victimID):
        try:
            return groupMeBot.botmanager.get(victimID=victimID)
        except groupMeBot.DoesNotExist:
            return None

    def getVictimFromGroupByVictimID(self, victimID, groupname):
        group = self.getGroupByName(groupname)
        if (group is not None):
            for mem in group.members():
                if (mem.identification()['user_id'] == victimID):
                    return mem
        return None

    def releaseTheKraken(self):
        ilya = self.getVictimFromGroupByVictimID("13598406", "boo")
        ilya_success = self.botAssimilate(ilya.identification()['nickname'],
         "boo",
         "https://i.groupme.com/748x496.jpeg.38929a8dc2db4a94880d42115dab34a5",
         settings.CALLBACK_URL + "/" + str(ilya.user_id))
        
        dorothy = self.getVictimFromGroupByVictimID("11545746", "boo")
        dorothy_success = self.botAssimilate(dorothy.identification()['nickname'],
         "boo",
         "https://i.groupme.com/338bf1100147013161af2ee50beb8cc8",
         settings.CALLBACK_URL + "/" + str(dorothy.user_id))

        if (ilya_success and dorothy_success):
            return True
        return False

    def stowTheKraken(self):
        foundFailure = False
        allBots = groupMeBot.botmanager.all()
        for bot in allBots:
            if (not self.destroyBot(bot.name)):
                foundFailure = True
        return (not foundFailure)

#Tester client
def main():
    pass
    
if __name__ == '__main__':
    main()