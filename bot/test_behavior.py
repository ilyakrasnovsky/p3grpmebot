from django.test import TestCase
from bot.behavior import Behavior
from bot.models import groupMeBot
import groupy

class TestBehavior(TestCase):
	def setUp(self):
		myBehavior = Behavior()
		myBehavior.stowTheKraken()

	def test_000_meMyselfAndI(self):
		#groupyAPI is working
		myBehavior = Behavior()
		self.assertEqual(str(myBehavior.meMyselfAndI().name), 'Ilya Krasnovsky')

	def test_001_getGroupByName(self):
		myBehavior = Behavior()
		#group hit
		self.assertEqual(str(myBehavior.getGroupByName("boo").group_id), '25434001')
		#group miss
		self.assertIsNone(myBehavior.getGroupByName("wah"))

	def test_002_getGroupByID(self):
		myBehavior = Behavior()
		#group hit
		self.assertEqual(str(myBehavior.getGroupByID("25434001").name), 'boo')
		#group miss
		self.assertIsNone(myBehavior.getGroupByID("47239487"))

	def test_003_getVictimFromGroup(self):
		myBehavior = Behavior()
		#member and group hit
		self.assertEqual(str(myBehavior.getVictimFromGroup("Dorothy Tang", "boo").identification()['nickname']), 'Dorothy Tang')
		#member miss
		self.assertIsNone(myBehavior.getVictimFromGroup("Ilya", "Tests"))
		#group miss
		self.assertIsNone(myBehavior.getVictimFromGroup("Ilya Krasnovsky", "wah"))
		
		#bot member and group hit, exclude bot
		self.assertIsNone(myBehavior.getVictimFromGroup("Dorothy Tang ", "boo"))
		#bot member miss
		self.assertIsNone(myBehavior.getVictimFromGroup("Fister Roboto", "boo"))
		#group miss with bot
		self.assertIsNone(myBehavior.getVictimFromGroup("Haiti Badding Sr ", "wah"))

	def test_004_addBot(self):
		myBehavior = Behavior()
		#success on name
		self.assertTrue(myBehavior.addBot(name="Dorothy Tang ",
		 								  groupname="Tests",
		 								  avatar_url="https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
		 								  callback_url="https://www.google.com",
										  victimID=1234))
		#failure on existing name
		self.assertFalse(myBehavior.addBot(name="Dorothy Tang ",
		 								  groupname="Tests",
		 								  avatar_url="https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
		 								  callback_url="https://www.google.com",
										  victimID=1234))
		#delete the bot from groupy without my api
		for bot in groupy.Bot.list():
			if (bot.name == "Dorothy Tang "):
				bot.destroy()
		#delete the bot from the database without my api
		groupMeBot.botmanager.removeBotByName("Dorothy Tang ")

	def test_005_getBot(self):
		myBehavior = Behavior()
		#make bot
		myBehavior.addBot(name="Dorothy Tang ",
						  groupname="Tests",
						  avatar_url="https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
						  callback_url="https://www.google.com",
						  victimID=1234)
		#bot hit
		self.assertEqual(str(myBehavior.getBot("Dorothy Tang ").name), 'Dorothy Tang ')
		#bot miss
		self.assertIsNone(myBehavior.getBot("Fister Roboto"))
		#delete the bot from groupy without my api
		for bot in groupy.Bot.list():
			if (bot.name == "Dorothy Tang "):
				bot.destroy()
		#delete the bot from the database without my api
		groupMeBot.botmanager.removeBotByName("Dorothy Tang ")

	def test_006_destroyBot(self):
		myBehavior = Behavior()
		#make a bot
		myBehavior.addBot(name="Dorothy Tang ",
						  groupname="Tests",
						  avatar_url="https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
						  callback_url="https://www.google.com",
						  victimID=1234)
		#successfully destroy it
		self.assertTrue(myBehavior.destroyBot("Dorothy Tang "))
		#fail to destroy it again because it was already destroyed
		self.assertFalse(myBehavior.destroyBot("Dorothy Tang "))

	def test_007_botAssimilate(self):
		myBehavior = Behavior()
		#make a bot in Tests to haunt user "Ilya Krasnovsky"
		self.assertTrue(myBehavior.botAssimilate(victimName="Ilya Krasnovsky",
												 groupname="Tests",
												 avatar_url="https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
												 callback_url="https://www.google.com"))
		#fail to haunt a nonexistent user
		self.assertFalse(myBehavior.botAssimilate(victimName="Dorothy Tang",
												 groupname="Tests",
												 avatar_url="https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
												 callback_url="https://www.google.com"))
		#fail to make more than one bot to haunt one user
		self.assertFalse(myBehavior.botAssimilate(victimName="Ilya Krasnovsky",
												 groupname="Tests",
												 avatar_url="https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
												 callback_url="https://www.google.com"))
		#fail to haunt a bot
		self.assertFalse(myBehavior.botAssimilate(victimName="Ilya Krasnovsky ",
												 groupname="Tests",
												 avatar_url="https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
												 callback_url="https://www.google.com"))
		#make the bot say something
		ilyabot = myBehavior.getBot("Ilya Krasnovsky ")
		ilyabot.post("Hi")
		#use my destroy function to destroy dtangbot
		myBehavior.destroyBot(ilyabot.name)

	'''NOT CURRENTLY SUPPORTED
	def test_008_changeMe(self):
		myBehavior = Behavior()
		#save my old name
		oldname = str(myBehavior.meMyselfAndI().name)
		#change my name
		self.assertTrue(myBehavior.changeMyName("I am Lord Voldemort", "Tests"))
		#fail to 

		#verfiy my name change
		self.assertEqual(str(myBehavior.meMyselfAndI().name), "I am Lord Voldemort")
		#change my name back
		myBehavior.changeMyName(oldname, "Tests")
	'''

	def test_009_botAdaptToNameChange(self):
		myBehavior = Behavior()
		#make a bot to haunt Ilya Krasnovsky in Tests
		myBehavior.botAssimilate(victimName="Ilya Krasnovsky",
								 groupname="Tests",
								 avatar_url="https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
								 callback_url="https://www.google.com")
		#fail to change the bot to wahbot because wahbot is not a victim
		self.assertFalse(myBehavior.botAdaptToNameChange("wahbot", "Ilya Krasnovsky"))
		#fail to change a bot if victim name was wrong
		self.assertFalse(myBehavior.botAdaptToNameChange("wahbot", "Dorothy Tang"))
		#destroy the bot
		myBehavior.destroyBot("Ilya Krasnovsky ")
		
		#make a bot to haunt Ilya Krasnovsky in boo
		myBehavior.botAssimilate(victimName="Ilya Krasnovsky",
								 groupname="boo",
								 avatar_url="https://i.groupme.com/748x496.jpeg.38929a8dc2db4a94880d42115dab34a5",
								 callback_url="https://www.google.com")
		#successfuly change the bot to haunt Dorothy Tang
		self.assertTrue(myBehavior.botAdaptToNameChange("Dorothy Tang", "Ilya Krasnovsky"))
		#destroy the bot
		myBehavior.destroyBot("Dorothy Tang ")

	def test_010_botAdaptToAvatarChange(self):
		myBehavior = Behavior()
		#make a bot to haunt Ilya Krasnovsky in Tests
		myBehavior.botAssimilate(victimName="Ilya Krasnovsky",
								 groupname="Tests",
								 avatar_url="https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
								 callback_url="https://www.google.com")
		#successfully change the bot's avatar image
		self.assertTrue(myBehavior.botAdaptToAvatarChange("Ilya Krasnovsky",
		 	"https://i.groupme.com/338bf1100147013161af2ee50beb8cc8"))
		#fail to change a bot if victim name was wrong
		self.assertFalse(myBehavior.botAdaptToAvatarChange("Dorothy Tang",
			"https://i.groupme.com/338bf1100147013161af2ee50beb8cc8"))
		#destroy the bot
		myBehavior.destroyBot("Ilya Krasnovsky ")
		
	def test_011_botBehave(self):
		myBehavior = Behavior()
		#make a bot to haunt Ilya Krasnovsky in Tests
		myBehavior.botAssimilate(victimName="Ilya Krasnovsky",
								 groupname="Tests",
								 avatar_url="https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
								 callback_url="https://www.google.com")
		#successfully get the bot to behave
		self.assertTrue(myBehavior.botBehave("Ilya Krasnovsky ", "How are you?"))
		#successfully get the bot to behave
		self.assertTrue(myBehavior.botBehave("Ilya Krasnovsky ", "How is the weather?"))
		#fail to get a nonexistent bot to behave
		self.assertFalse(myBehavior.botBehave("Dorothy Tang ", "How is the weather?"))
		#destroy the bot
		myBehavior.destroyBot("Ilya Krasnovsky ")

	def test_012_releaseTheKraken(self):
		myBehavior = Behavior()
		#try releasing the kraken, make sure bots are properly created
		self.assertTrue(myBehavior.releaseTheKraken())
		#make sure you can't do this twice
		self.assertFalse(myBehavior.releaseTheKraken())
		#destroy the created bots
		myBehavior.destroyBot("Ilya Krasnovsky ")
		myBehavior.destroyBot("Dorothy Tang ")
		
	def test_013_stowTheKraken(self):
		myBehavior = Behavior()
		#release the kraken first
		myBehavior.releaseTheKraken()
		#try stowing the kraken, make sure bots are properly deleted
		self.assertTrue(myBehavior.stowTheKraken())

	def test_014_getVictimByID(self):
		myBehavior = Behavior()
		#member hit
		self.assertEqual(str(myBehavior.getVictimByID("13598406").identification()['nickname']), 'Ilya Krasnovsky')
		#member miss
		self.assertIsNone(myBehavior.getVictimByID("34343434"))

	def test_015_getBotByVictimID(self):
		myBehavior = Behavior()
		#make a bot to haunt Ilya Krasnovsky in Tests
		myBehavior.botAssimilate(victimName="Ilya Krasnovsky",
								 groupname="Tests",
								 avatar_url="https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
								 callback_url="https://www.google.com")
		
		#bot hit
		self.assertEqual(myBehavior.getBotByVictimID(13598406).name, "Ilya Krasnovsky ")
		#bot miss
		self.assertIsNone(myBehavior.getBotByVictimID(3434343434))
		myBehavior.destroyBot("Ilya Krasnovsky ")

	def test_016_getVictimFromGroupByVictimID(self):
		myBehavior = Behavior()
		#make a bot to haunt Fister Roboto in Tests
		myBehavior.botAssimilate(victimName="Ilya Krasnovsky",
								 groupname="Tests",
								 avatar_url="https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
								 callback_url="https://www.google.com")
		
		#bot hit
		self.assertEqual(myBehavior.getVictimFromGroupByVictimID("13598406", "Tests").identification()['nickname'], "Ilya Krasnovsky")
		#bot miss
		self.assertIsNone(myBehavior.getVictimFromGroupByVictimID("3434343434", "Tests"))
		myBehavior.destroyBot("Ilya Krasnovsky ")