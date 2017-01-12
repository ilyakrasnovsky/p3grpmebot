'''
module : botmgr

features bot manager class called BotMgr, and Bot

'''

import dbmgr
import requests
from django.conf import settings

import localcreds

'''
class: BotMgr

description:
    - bot manager class

attributes:
    db : instance of the dbmgr class    


initializer input:
    None

functions:
    registerBot()
    unregisterBot()
    configureBot()

'''

class BotMgr():
    def __init__(self):
        self.db = dbmgr.Dbmgr()
        #self.groupMeKey = settings.GROUPMEBOT_GROUPME_SECRET_KEY
        self.groupmeurl = "fakeurl"
        self.groupMeKey = localcreds.get_credentials(groupme=True)
    '''
    function: registerBot()

    description:
        -Registers a bot with groupMe and adds it to the database if the
        registration was successful

    inputs: 
        botname : name for the bot (string)
        group_id : groupme group id (string) to put the bot into

    outputs:
        status : True if addition was successful,
                False if name of offender already taken,
                "ERROR" (string) in the case of connection
                issue or authentication problem.
    '''
    def registerBot(self, botname, group_id):
        requests.post()

        isPresent = self.getUser(username)
        if (isPresent == None):
            try:
                self.fdb.put('/users/', username, {"messages" : [""]})
                return True
            except HTTPError:
                return "ERROR"
        elif (isPresent == "ERROR"):
            return "ERROR"
        else:
            return False

    '''
    function: getUser()

    description:
        -Searches for a user in the database from a name,
        DEFAULT gets all users

    inputs: 
        username : name (string) of a user to look for (optional, if None,
            returns all users)

    outputs:
         If found, returns dictionary representing an user
         (or dictionary of dictionaries of many users by name
            if name was None, None if not found, and "ERROR" if 
                connection/authentication issue)
    '''
    def getUser(self,username=None):
        try:
            return self.fdb.get('/users/', username)
        except HTTPError:
            return "ERROR"

    '''
    function: removeUser()

    description:
        -Removes an offender from the database by name

    inputs: 
        username : name (string) of offender to delete
        
    outputs:
        status : True if delete was successful,
                False if selected offender not in database,
                "ERROR" (string) in the case of connection
                issue or authentication problem.
    '''
    def removeUser(self, username):
        isPresent = self.getUser(username)
        if (isPresent != None):
            try:
                self.fdb.delete('/users/', username)
                return True
            except HTTPError:
                return "ERROR"
        elif (isPresent == "ERROR"):
            return "ERROR"
        else:
            return False

    '''
    function: addMessage()

    description:
        -Adds a message (string) to the database.

    inputs: 
        username: a string of user name
        message : a string of the message to be added

    outputs:
        status : True if addition was successful,
                "ERROR" (string) in the case of connection
                issue or authentication problem.
    '''
    def addMessage(self, username, message):
        isPresent = self.getUser(username)
        if (isPresent != None):
            try:
                isPresent['messages'].append(message)
                self.fdb.patch('/users/' + username, isPresent)
                return True
            except HTTPError:
                print ("wtf")
                return "ERROR"
        elif (isPresent == "ERROR"):
            return "ERROR"
        else:
            temp = self.addUser(username)
            if (temp != "ERROR"):
                self.addMessage(username, message)
                return True

    '''
    function: addBot()

    description:
        -Adds a bot to the database

    inputs: 
        botname : name (string) of bot to add
        botid : the bot id (string from groupme) of bot to add

    outputs:
        True if successful, False if bot name already taken,
        and "ERROR" if connection/authentication issue)
    '''
    def addBot(self, botname, botid):
        isPresent = self.getBot(botname)
        if (isPresent == None):
            try:
                self.fdb.put('/bots/', botname, {"id" : botid})
                return True
            except HTTPError:
                return "ERROR"
        elif (isPresent == "ERROR"):
            return "ERROR"
        else:
            return False

    '''
    function: getBot()

    description:
        -retrieves bot information from database by name

    inputs: 
        botname : name (string) of bot to retrieve, if None, returns dict
        of all bots in database
        
    outputs:
        status : dict of bot info (or dict of such dicts if botname == None),
                "ERROR" (string) in the case of connection
                issue or authentication problem.
    '''
    def getBot(self, botname=None):
        try:
            return self.fdb.get('/bots/', botname)
        except HTTPError:
            return "ERROR"

    '''
        function: removeBot()

        description:
            -Removes a bot from the database by name

        inputs: 
            botname : name (string) of bot to delete
            
        outputs:
            status : True if delete was successful,
                    False if selected bot not in database,
                    "ERROR" (string) in the case of connection
                    issue or authentication problem.
    '''
    def removeBot(self, botname):
        isPresent = self.getBot(botname)
        if (isPresent != None):
            try:
                self.fdb.delete('/bots/', botname)
                return True
            except HTTPError:
                return "ERROR"
        elif (isPresent == "ERROR"):
            return "ERROR"
        else:
            return False
   
#Tester client
def main():
    botmgr1 = BotMgr()    

if __name__ == '__main__':
    main()