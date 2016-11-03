from django.test import TestCase
from bot.dbmgr import PDbmgr

class TestPDbmgr(TestCase):
	def setUp(self):
		pass
	
	def test_000_addBot(self):
		pdbmgr = PDbmgr()
		#success on name
		self.assertTrue(pdbmgr.addBot("Dorothy Tang ", "dtang_bot_id", "https://www.google.com", "https://www.google.com"))
		#failure on existing name
		self.assertFalse(pdbmgr.addBot("Dorothy Tang ", "dtang_bot_id1", "https://www.google.com", "https://www.google.com"))
		#failure on existing id
		self.assertFalse(pdbmgr.addBot("Fister Roboto", "dtang_bot_id", "https://www.google.com", "https://www.google.com"))
		#failure on invalid fields (ex invalid URL)
		self.assertFalse(pdbmgr.addBot("Fister Roboto", "fister_roboto_id", "fake_url", "fake_url"))

	def test_001_getBotByName(self):
		pdbmgr = PDbmgr()
		pdbmgr.addBot("Dorothy Tang ", "dtang_bot_id", "https://www.google.com", "https://www.google.com")
		#bot hit
		self.assertEqual(str(pdbmgr.getBotByName("Dorothy Tang ").name), 'Dorothy Tang ')
		#bot miss
		self.assertIsNone(pdbmgr.getBotByName("Fister Roboto"))

	def test_002_getBotByID(self):
		pdbmgr = PDbmgr()
		pdbmgr.addBot("Dorothy Tang ", "dtang_bot_id", "https://www.google.com", "https://www.google.com")
		#bot hit
		self.assertEqual(str(pdbmgr.getBotByID("dtang_bot_id").name), 'Dorothy Tang ')
		#bot miss
		self.assertIsNone(pdbmgr.getBotByID("fister_roboto_id"))



	