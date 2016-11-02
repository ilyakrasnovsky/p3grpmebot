from django.test import TestCase
from bot.dbmgr import PDbmgr

class TestPDbmgr(TestCase):
	def setUp(self):
		pass
	
	def test_000_addBot(self):
		pdbmgr = PDbmgr()
		self.assertTrue(pdbmgr.addBot("Dorothy Tang ", "dtang_bot_id", "www.google.com", "www.google.com"))
		self.assertFalse()

	def test_001_getBotByName(self):
		pdbmgr = PDbmgr()
		#bot hit
		self.assertEqual(str(pdbmgr.getBotByName("Dorothy Tang ").name), 'Dorothy Tang ')
		#bot miss
		self.assertIsNone(pdbmgr.getBotByName("Fister Roboto"))

	def test_002_getBotByID(self):
		pdbmgr = PDbmgr()
		#bot hit
		self.assertEqual(str(pdbmgr.getBotByID("dtang_botid").name), 'Dorothy Tang ')
		#bot miss
		self.assertIsNone(pdbmgr.getBotByID("fister_roboto_botid"))



	