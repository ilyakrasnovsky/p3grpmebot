'''
module : dbclient (database client)

supports client class for dbmgr

classes:
	DbClient
'''

from dbmgr import Dbmgr
import getpass
import dbutils

'''
class: DbClient

description:
    -acts as a client for dbmgr module, features higher level
    functions

attributes:
	dbmgr : instance of the Dbmgr class

initializer input:
	dbmgr : instance of the Dbmgr class

functions:
	registerOffender()
	changeOffender()
	unregisterOffender()

'''

class DbClient():
	def __init__(self, dbmgr):
		self.dbmgr = dbmgr
		myname = getpass.getuser()
		print ("Welcome to Crass! You're such an asshole."
			   " Registering you as an offender ...")
		print
		status = self.registerOffender(myname)
		if (status == False):
			print ("Oh wait, it looks like you're fucking in here"
				" already. Bullshit. Well, good for you, asshole.")
		else:
			print ("Done! Do you feel good about yourself?")

	'''
    function: registerOffender()

    description:
        -Registers a Crass offender in the database with default
        attributes (5,5,5,5)

    inputs: 
        name : A string name of the offender to be Registers

    outputs:
    	status : True if addition worked, False if name already
    	registered, and "ERROR" in case of connection/authentication
    	issue
    '''
	def registerOffender(self, name):
		newOffender = {
			"name" : name,
			"attr" : {
		        'speed' : 5,
		        'accuracy' : 5,
		        'readability' : 5,
		        'confidence' : 5 
			}
		}
		return self.dbmgr.addOffender(newOffender)
		
	'''
    function: changeOffender()

    description:
        -Changes another offender's attributes

    inputs: 
        name : A string name of the offender to be changed
        attr : a dictionary of the form 
        		{
        			'speed' : int,
        			'accuracy' : int,
        			'readability' : int,
        			'confidence' : int 
        		}
    outputs:
    	status : True if change worked, False if not in database or
    	if it is yourself, and "ERROR" in case of connection/authentication
    	issue
    '''
	def changeOffender(self, name, attr):
		#check to make sure that that the offender you're
		#changing is not you
		if (name == getpass.getuser()):
			print ("You're trying to change information about yourself!?"
					" WTF?! You can't do that.")
			return False
		else:
			return self.dbmgr.updateOffender(name, attr)

	'''
    function: unregisterOffender()

    description:
        -A bit of an easter egg of crass. This function will
        only unregister a crass offender if it is called with
        a key-word argument fuckyou=<nametounregister>

    inputs: 
        None (or fuckyou=<name>)

    outputs:
    	status : True if successful, False if not in database or
    	fuckyou key-word not provided, "ERROR" IF connection/authentication
    	issue
    '''
	def unregisterOffender(self, **kwargs):
		if kwargs.has_key("fuckyou"):
			return self.dbmgr.removeOffender(kwargs["fuckyou"])
		else:
			print ("No can do. Offenders are registered for life.")
			return False
			
	'''
    function: findFellowOffenders()

    description:
        -Gets a list of fellow offender names to interact with

    inputs: 
        None

    outputs:
    	names of offenders as a list, or None if you're alone on
    	Crass
    '''
	def findFellowOffenders(self):
		offenders = self.dbmgr.getOffender()
		if (len(offenders.keys()) > 1):
			print ("Your 'honorary' fellow offenders are : ")
			return offenders.keys()
		else:
			print ("Looks like you're the only bitch on Crass right now.")
			return None

	'''
    function: learnVocabulary()

    description:
        -Gets a list of currently key-worded crass words

    inputs: 
        None

    outputs:
    	list of words on Crass, or None if no words currently key-worded
    '''
	def learnVocabulary(self):
		return self.dbmgr.getCrassWord().keys()
		
#Tester client
def main():
	dbmgr = Dbmgr()
	dbclient = DbClient(dbmgr)
	print (dbclient.findFellowOffenders()) 
	print
	print (dbclient.learnVocabulary())
	print
	print (dbclient.unregisterOffender())
	print
	print (dbclient.unregisterOffender(fuckyou="Hannah"))
	print 
	change = {
    			'speed' : 1,
    			'accuracy' : 1,
    			'readability' : 1,
    			'confidence' : 1 
       	} 
	print (dbclient.changeOffender("ilya", change))
	print
	print (dbclient.changeOffender("Danny", change))
	#valid = False	
	#while(valid != True):
	#	welcome = input()

if __name__ == '__main__':
    main()