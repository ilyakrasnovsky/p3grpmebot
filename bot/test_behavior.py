from django.test import TestCase
from bot import behavior

class meMyselfAndITestCase(TestCase):
	def test_meMyselfAndI(self):
		self.assertEqual(str(behavior.meMyselfAndI()), 'Ilya Krasnovsky')

class getBotTestCase(TestCase):
	def test_getBot(self):
		self.assertEqual(str(behavior.getBot("Dorothy Tang ").bot_id), '000ccdb6b4bd1320e186cdc10f')
		self.assertIsNone(behavior.getBot("Fister Roboto"))

class getGroupTestCase(TestCase):
	def test_getGroup(self):
		self.assertEqual(str(behavior.getGroup("boo").group_id), '25434001')
		self.assertIsNone(behavior.getGroup("wah"))

