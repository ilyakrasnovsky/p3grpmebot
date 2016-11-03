from django.test import TestCase
from bot.models import groupMeBot

class TestModels(TestCase):
	def setUp(self):
		pass
	
	def test_000_addBot(self):
		#success on name
		self.assertTrue(groupMeBot.botmanager.addBot("Dorothy Tang ", "dtang_bot_id", "Tests", "https://www.google.com", "https://www.google.com"))
		#failure on existing name
		self.assertFalse(groupMeBot.botmanager.addBot("Dorothy Tang ", "dtang_bot_id1", "Tests", "https://www.google.com", "https://www.google.com"))
		#failure on existing id
		self.assertFalse(groupMeBot.botmanager.addBot("Fister Roboto", "dtang_bot_id", "Tests", "https://www.google.com", "https://www.google.com"))
		#failure on invalid fields (ex invalid URL)
		self.assertFalse(groupMeBot.botmanager.addBot("Fister Roboto", "fister_roboto_id", "Tests", "fake_url", "fake_url"))

	def test_001_getBotByName(self):
		groupMeBot.botmanager.addBot("Dorothy Tang ", "dtang_bot_id", "Tests", "https://www.google.com", "https://www.google.com")
		#bot hit
		self.assertEqual(str(groupMeBot.botmanager.getBotByName("Dorothy Tang ").name), 'Dorothy Tang ')
		#bot miss
		self.assertIsNone(groupMeBot.botmanager.getBotByName("Fister Roboto"))

	def test_002_getBotByID(self):
		groupMeBot.botmanager.addBot("Dorothy Tang ", "dtang_bot_id", "Tests", "https://www.google.com", "https://www.google.com")
		#bot hit
		self.assertEqual(str(groupMeBot.botmanager.getBotByID("dtang_bot_id").name), 'Dorothy Tang ')
		#bot miss
		self.assertIsNone(groupMeBot.botmanager.getBotByID("fister_roboto_id"))

	def test_003_removeBotByName(self):
		groupMeBot.botmanager.addBot("Dorothy Tang ", "dtang_bot_id", "Tests", "https://www.google.com", "https://www.google.com")
		#bot hit
		self.assertTrue(groupMeBot.botmanager.removeBotByName("Dorothy Tang "))
		#bot miss
		self.assertFalse(groupMeBot.botmanager.removeBotByName("Fister Roboto"))

	def test_004_removeBotID(self):
		groupMeBot.botmanager.addBot("Dorothy Tang ", "dtang_bot_id", "Tests", "https://www.google.com", "https://www.google.com")
		#bot hit
		self.assertTrue(groupMeBot.botmanager.removeBotByID("dtang_bot_id"))
		#bot miss
		self.assertFalse(groupMeBot.botmanager.removeBotByID("fister_roboto_id"))
	



	

	