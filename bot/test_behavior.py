from django.test import TestCase
from bot.behavior import Behavior
import groupy

class TestBehavior(TestCase):
	def setUp(self):
		pass

	def test_000_meMyselfAndI(self):
		#groupyAPI is working
		myBehavior = Behavior()
		self.assertEqual(str(myBehavior.meMyselfAndI().name), 'Ilya Krasnovsky')

	def test_001_getGroup(self):
		myBehavior = Behavior()
		#group hit
		self.assertEqual(str(myBehavior.getGroup("boo").group_id), '25434001')
		#group miss
		self.assertIsNone(myBehavior.getGroup("wah"))

	def test_002_getVictimFromGroup(self):
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

	def test_003_addBot(self):
		myBehavior = Behavior()
		#success on name
		self.assertTrue(myBehavior.addBot("Dorothy Tang ",
		 "Tests",
		 "https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
		 "https://www.google.com"))
		#failure on existing name
		self.assertFalse(myBehavior.addBot("Dorothy Tang ",
		 "Tests",
		 "https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
		 "https://www.google.com"))
		#delete the bot from groupy without my api
		for bot in groupy.Bot.list():
			if (bot.name == "Dorothy Tang "):
				bot.destroy()

	def test_004_getBot(self):
		myBehavior = Behavior()
		#make bot
		myBehavior.addBot("Dorothy Tang ",
		 "Tests",
		 "https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
		 "https://www.google.com")
		#bot hit
		self.assertEqual(str(myBehavior.getBot("Dorothy Tang ").name), 'Dorothy Tang ')
		#bot miss
		self.assertIsNone(myBehavior.getBot("Fister Roboto"))
		#delete the bot from groupy without my api
		for bot in groupy.Bot.list():
			if (bot.name == "Dorothy Tang "):
				bot.destroy()		

	def test_005_destroyBot(self):
		myBehavior = Behavior()
		#make a bot
		myBehavior.addBot("Dorothy Tang ",
		 "Tests",
		 "https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
		 "https://www.google.com")
		#successfully destroy it
		self.assertTrue(myBehavior.destroyBot("Dorothy Tang "))
		#fail to destroy it again because it was already destroyed
		self.assertFalse(myBehavior.destroyBot("Dorothy Tang "))

	def test_006_botAssimilate(self):
		myBehavior = Behavior()
		#make a bot in boo to haunt user "Dorothy Tang"
		self.assertTrue(myBehavior.botAssimilate("Ilya Krasnovsky",
			"Tests",
			"https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
			"https://www.google.com"))
		#fail to haunt a nonexistent user
		self.assertFalse(myBehavior.botAssimilate("Dorothy Tang",
			"Tests",
			"https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
			"https://www.google.com"))
		#fail to make more than one bot to haunt one user
		self.assertFalse(myBehavior.botAssimilate("Ilya Krasnovsky",
			"Tests",
			"https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
			"https://www.google.com"))
		#fail to haunt a bot
		self.assertFalse(myBehavior.botAssimilate("Ilya Krasnovsky ",
			"boo",
			"https://i.groupme.com/640x640.jpeg.8dc11c99ffe644ba967be36ab06015eb",
			"https://www.google.com"))
		#make the bot say something
		ilyabot = myBehavior.getBot("Ilya Krasnovsky ")
		ilyabot.post("Hi")
		#use my destroy function to destroy dtangbot
		myBehavior.destroyBot(ilyabot.name)

	def test_007_changeMe(self):
		myBehavior = Behavior()
		#save my old name
		oldname = str(myBehavior.meMyselfAndI().name)
		#change my name
		self.assertTrue(myBehavior.changeMe("I am Lord Voldemort"))
		#fail to 

		#verfiy my name change
		self.assertEqual(str(myBehavior.meMyselfAndI().name), "I am Lord Voldemort")
		#change my name back
		myBehavior.changeMe(oldname)

