from django.test import TestCase
from bot.behavior import Behavior

class TestBehavior(TestCase):
	def setUp(self):
		pass

	def test_000_meMyselfAndI(self):
		#groupyAPI is working
		myBehavior = Behavior()
		self.assertEqual(str(myBehavior.meMyselfAndI()), 'Ilya Krasnovsky')

	def test_001_addBot(self):
		myBehavior = Behavior()
		#success on name
		self.assertTrue(myBehavior.addBot("Dorothy Tang ", "Tests"))

	def test_001_getBot(self):
		myBehavior = Behavior()
		#bot hit
		self.assertEqual(str(myBehavior.getBot("Dorothy Tang ").bot_id), '000ccdb6b4bd1320e186cdc10f')
		#bot miss
		self.assertIsNone(myBehavior.getBot("Fister Roboto"))

	def test_002_getGroup(self):
		myBehavior = Behavior()
		#group hit
		self.assertEqual(str(myBehavior.getGroup("boo").group_id), '25434001')
		#group miss
		self.assertIsNone(myBehavior.getGroup("wah"))

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

	'''
	def test004_botAssimilate(self):
		myBehavior = Behavior()
		#make a bot in Tests to haunt user "Ilya Krasnovsky"
		self.assertTrue(True)
	'''

	'''
	def test_005_destroyBot(self):
		myBehavior = Behavior()
		destroyMe = myBehavior.getBot("Dorothy Tang")
		myBehavior.destroyBot()
	'''
