'''
module : behavior

has common/helpful bot behavior routines

'''

import groupy
from bot.models import groupMeBot

class Behavior():
	def __init__(self):
		pass

	#get information about myself
	def meMyselfAndI(self):
		return groupy.User.get()

	#get an existing bot by name (string)
	#returns Bot instance (groupy API) if found,
	#None if not
	def getBot(self, botname):
		modelbot = groupMeBot.botmanager.getBotByName(botname)
		if (modelbot is not None):
			for mybot in groupy.Bot.list():
				if (mybot.name == botname):
					return mybot
		return None

	#make a bot to haunt victimName (string) in groupName (string)
	#with avatar_url (groupMe URL as string) and callback_url
	#returns True if successful, False if not
	def botAssimilate(self, victimName, groupName, avatar_url, callback_url):
		if (self.getVictimFromGroup(victimName, groupName) is not None):
			if (self.addBot(victimName + " ", groupName, avatar_url, callback_url)):
				return True
		return False

	def addBot(self, botname, groupName, avatar_url, callback_url):
		if (groupMeBot.botmanager.getBotByName(botname) is None):
			try:
				newbot = groupy.Bot.create(botname, 
								  self.getGroup(groupName),
								  avatar_url,
								  callback_url)
				if (groupMeBot.botmanager.addBot(newbot.name,
				 								 newbot.bot_id,
				 								 groupName,
				 								 newbot.avatar_url,
				 								 newbot.callback_url) == False):
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
	def getGroup(self, groupName):
		for group in groupy.Group.list(): 
			if(group.name == groupName):
				return group
		return None

	#Finds a victim whose name is victimName(string)
	#in the groupme group given by groupName. returns
	#Member instance (groupy API) if found, None if not
	def getVictimFromGroup(self, victimName, groupName):
		group = self.getGroup(groupName)
		if (group is not None):
			for mem in group.members():
				if (mem.identification()['nickname'] == victimName):
					return mem
		return None

#Tester client
def main():
	pass
	
if __name__ == '__main__':
    main()