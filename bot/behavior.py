'''
module : behavior

has common/helpful bot behavior routines

'''

import groupy
#from bot import dbmgr
#import dbmgr

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
		for mybot in groupy.Bot.list():
			if (mybot.name == botname):
				return mybot
		return None

	#make a bot to haunt victimName (string) in groupName (string)
	#with avatar_url (groupMe URL as string) and callback_url
	#returns True if successful, False if not
	def botAssimilate(self, victimName, groupName, avatar_url, callback_url):
		if (self.getVictimFromGroup(victimName, groupName) is not None):
			try:
				groupy.Bot.create(victimName + " ", 
								  self.getGroup(groupName),
								  avatar_url,
								  callback_url)
				return True
			except groupy.api.errors.ApiError:
				return False
		return False

	#destroy the bot given by botname (string), if it exists
	def destroyBot(self, botname):
		bot_to_destroy = self.getBot(botname)
		if (bot_to_destroy is not None):
			bot_to_destroy.destroy()

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
	print (meMyselfAndI())
	
	if (getBot("Dorothy Tang ") is not None):
		print (getBot("Dorothy Tang ").bot_id)
	else:
		print ("Dorothy Tang is not a bot")

	if (getBot("Fister Roboto") is not None):
		print (getBot("Fister Roboto").bot_id)
	else:
		print ("Fister Roboto is not a bot")
	
	if (getGroup("boo") is not None):
		print (getGroup("boo").group_id)
	else:
		print ("boo is not a group")

	if (getGroup("wah") is not None):
		print (getGroup("wah").group_id)
	else:
		print ("wah is not a group")

	if (getVictimFromGroup("Dorothy Tang", "boo") is not None):
		print (getVictimFromGroup("Dorothy Tang", "boo").identification()['nickname'])
	else:
		print ("Dorothy Tang is not in group boo, or group boo doesn't exist")

	if (getVictimFromGroup("Haiti Badding Sr ", "Tests") is not None):
		print (getVictimFromGroup("Haiti Badding Sr ", "Tests").identification()['nickname'])
	else:
		print ("Haiti Badding Sr is not in group Tests, or group Tests doesn't exist")

	if (getVictimFromGroup("Ilya", "Tests") is not None):
		print (getVictimFromGroup("Ilya", "Tests").identification()['nickname'])
	else:
		print ("Ilya is not in group Tests, or group Tests doesn't exist")

	if (getVictimFromGroup("Ilya Krasnovsky", "Tests") is not None):
		print (getVictimFromGroup("Ilya Krasnovsky", "Tests").identification()['nickname'])
	else:
		print ("Ilya Krasnovsky is not in group Tests, or group Tests doesn't exist")

	if (getVictimFromGroup("Dorothy Tang", "Tests") is not None):
		print (getVictimFromGroup("Dorothy Tang", "Tests").identification()['nickname'])
	else:
		print ("Dorothy Tang is not in group Tests, or group Tests doesn't exist")

	if (botAssimilate("Dorothy", "Tests", None, None)):
		print ("Created Dorothy bot in group Tests")
	else:
		print ("Failed to create Dorothy bot in group Tests")

	if (botAssimilate("Dorothy Tang", "boo", None, "https://ilyasgroupmebot.herokuapp.com/boobot0")):
		print ("Created Dorothy Tang bot in group boo")
	else:
		print ("Failed to create Dorothy Tang bot in group boo")

	if (botAssimilate("Ilya Krasnovsky", "boo", None, "https://ilyasgroupmebot.herokuapp.com/boobot1")):
		print ("Created Ilya Krasnovsky bot in group boo")
	else:
		print ("Failed to create Ilya Krasnovsky bot in group boo")

	if (botAssimilate("Ilya Krasnovsky", "boo", None, "https://ilyasgroupmebot.herokuapp.com/boobot2")):
		print ("Created Ilya Krasnovsky bot in group boo")
	else:
		print ("Failed to create Ilya Krasnovsky bot in group boo")

	if (botAssimilate("Ilya Krasnovsky", "Tests", None, None)):
		print ("Created Ilya Krasnovsky bot in group Tests")
	else:
		print ("Failed to create Ilya Krasnovsky bot in group Tests")


if __name__ == '__main__':
    main()