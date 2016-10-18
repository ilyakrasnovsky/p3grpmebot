from django.test import TestCase
from bot import behavior

class meMyselfAndITestCase(TestCase):
	def test_meMyselfAndI(self):
		#groupyAPI is working
		self.assertEqual(str(behavior.meMyselfAndI()), 'Ilya Krasnovsky')

class getBotTestCase(TestCase):
	def test_getBot(self):
		#bot hit
		self.assertEqual(str(behavior.getBot("Dorothy Tang ").bot_id), '000ccdb6b4bd1320e186cdc10f')
		#bot miss
		self.assertIsNone(behavior.getBot("Fister Roboto"))

class getGroupTestCase(TestCase):
	def test_getGroup(self):
		#group hit
		self.assertEqual(str(behavior.getGroup("boo").group_id), '25434001')
		#group miss
		self.assertIsNone(behavior.getGroup("wah"))

class getVictimFromGroupTestCase(TestCase):
	def test_getVictimFromGroup(self):
		#member and group hit
		self.assertEqual(str(behavior.getVictimFromGroup("Dorothy Tang", "boo").identification()['nickname']), 'Dorothy Tang')
		#member miss
		self.assertIsNone(behavior.getVictimFromGroup("Ilya", "Tests"))
		#group miss
		self.assertIsNone(behavior.getVictimFromGroup("Ilya Krasnovsky", "wah"))
		
		#bot member and group hit, exclude bot
		self.assertIsNone(behavior.getVictimFromGroup("Dorothy Tang ", "boo"))
		#bot member miss
		self.assertIsNone(behavior.getVictimFromGroup("Fister Roboto", "boo"))
		#group miss with bot
		self.assertIsNone(behavior.getVictimFromGroup("Haiti Badding Sr ", "wah"))
