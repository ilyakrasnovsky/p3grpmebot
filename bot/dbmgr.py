'''
module : dbmgr

features firebase wrapper class called Dbmgr

'''

from firebase import firebase
from requests import HTTPError
from django.conf import settings

#import localcreds

'''
class: Dbmgr

description:
    - database manager class

attributes:
    fdb : instance of the FirebaseApplication class    

initializer input:
    None

functions:
    addUser()
    getUser()
    removeUser()
    addMessage()
    addBot()
    getBot()
    removeBot()
'''

class Dbmgr():
    def __init__(self):
        #Authentication 
        FIREBASE_URL = settings.FIREBASE_URL # 
        FIREBASE_KEY = settings.GROUPMEBOT_FIREBASE_SECRET_KEY #localcreds.get_credentials(firebase=True) 
        #FIREBASE_URL = "https://groupmebot-4104f.firebaseio.com/" 
        #FIREBASE_KEY = localcreds.get_credentials(firebase=True) 
        
        authentication = firebase.FirebaseAuthentication(FIREBASE_KEY, 'ilyakrasnovsky@gmail.com', admin = True)
        self.fdb = firebase.FirebaseApplication(FIREBASE_URL, authentication=authentication)

    '''
    function: addUser()

    description:
        -Adds a groupMe user to the database from a dictionary
        of values

    inputs: 
        username : A string of username

    outputs:
        status : True if addition was successful,
                False if name of offender already taken,
                "ERROR" (string) in the case of connection
                issue or authentication problem.
    '''
    def addUser(self,username):
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
    dbmgr1 = Dbmgr()
    
    status = dbmgr1.addUser("ilya")
    print ("dbmgr1.addUser(ilya) status : " + str(status))
    
    status = dbmgr1.addUser("dorothy")
    print ("dbmgr1.addUser(dorothy) status : " + str(status))
    
    status = dbmgr1.addUser("dorothy")
    print ("dbmgr1.addUser(dorothy) (again) status : " + str(status))

    status = dbmgr1.getUser("dorothy")
    print ("dbmgr1.getUser(dorothy) status : " + str(status))
    
    status = dbmgr1.getUser("lol")
    print ("dbmgr1.getUser(lol) status : " + str(status))

    status = dbmgr1.getUser()
    print ("dbmgr1.getUser() status : " + str(status))

    status = dbmgr1.removeUser("ilya")
    print ("dbmgr1.removeUser(ilya) status : " + str(status))

    status = dbmgr1.removeUser("lol1")
    print ("dbmgr1.removeUser(lol1) status : " + str(status))

    status = dbmgr1.getUser("ilya")
    print ("dbmgr1.getUser(ilya) status : " + str(status))

    status = dbmgr1.addMessage("dorothy", "hi")
    print ("dbmgr1.addMessage(dorothy, hi) status : " + str(status))

    status = dbmgr1.addMessage("dorothy", "hi")
    print ("dbmgr1.addMessage(dorothy, hi) status : " + str(status))

    status = dbmgr1.addMessage("lol", "hi")
    print ("dbmgr1.addMessage(lol, hi) status : " + str(status))

    status = dbmgr1.addMessage("ilya", "i'm added via addMessage!")
    print ("dbmgr1.addMessage(ilya, i'm added via addMessage!) status : " + str(status))

    status = dbmgr1.getBot("ilyasbot")
    print ("dbmgr1.getBot(ilyasbot) status : " + str(status))

    status = dbmgr1.addBot("ilyasbot", "lololol")
    print ("dbmgr1.addBot(ilyasbot, lololol)" + str(status))

    status = dbmgr1.getBot("ilyasbot")
    print ("dbmgr1.getBot(ilyasbot) status : " + str(status))

    status = dbmgr1.removeBot("ilyasbot")
    print ("dbmgr1.removeBot(ilyasbot) status : " + str(status))    

if __name__ == '__main__':
    main()