from django.test import TestCase
from bot.models import groupMeBot

class TestModels(TestCase):
	def setUp(self):
		pass
	
	def test_000_addBot(self):
		#success on name
		self.assertTrue(groupMeBot.botmanager.addBot(name="Dorothy Tang ",
													 botID="dtang_bot_id",
													 victimID=1234,
													 groupname="Tests",
													 avatar_url="https://www.google.com",
													 callback_url="https://www.google.com"))
		#failure on existing name
		self.assertFalse(groupMeBot.botmanager.addBot(name="Dorothy Tang ",
													 botID="dtang_bot_id1",
													 victimID=12345,
													 groupname="Tests",
													 avatar_url="https://www.google.com",
													 callback_url="https://www.google.com"))
		#failure on existing botID
		self.assertFalse(groupMeBot.botmanager.addBot(name="Fister Roboto",
													 botID="dtang_bot_id",
													 victimID=12345,
													 groupname="Tests",
													 avatar_url="https://www.google.com",
													 callback_url="https://www.google.com"))
		#failure on existing victimID
		self.assertFalse(groupMeBot.botmanager.addBot(name="Fister Roboto",
													 botID="fister_roboto_id",
													 victimID=1234,
													 groupname="Tests",
													 avatar_url="https://www.google.com",
													 callback_url="https://www.google.com"))		
		#failure on invalid fields (ex invalid URL)
		self.assertFalse(groupMeBot.botmanager.addBot(name="Fister Roboto",
													 botID="fister_roboto_id",
													 victimID=12345,
													 groupname="Tests",
													 avatar_url="fake_url",
													 callback_url="fake_url"))		
		#failure on invalid fields (ex non-integer victimID)
		self.assertFalse(groupMeBot.botmanager.addBot(name="Fister Roboto",
													 botID="fister_roboto_id",
													 victimID="lolol",
													 groupname="Tests",
													 avatar_url="fake_url",
													 callback_url="fake_url"))		

	def test_001_getBotByName(self):
		groupMeBot.botmanager.addBot(name="Dorothy Tang ",
									 botID="dtang_bot_id",
									 victimID=1234,
									 groupname="Tests",
									 avatar_url="https://www.google.com",
									 callback_url="https://www.google.com")
		#bot hit
		self.assertEqual(str(groupMeBot.botmanager.getBotByName("Dorothy Tang ").name), 'Dorothy Tang ')
		#bot miss
		self.assertIsNone(groupMeBot.botmanager.getBotByName("Fister Roboto"))

	def test_002_getBotByID(self):
		groupMeBot.botmanager.addBot(name="Dorothy Tang ",
									 botID="dtang_bot_id",
									 victimID=1234,
									 groupname="Tests",
									 avatar_url="https://www.google.com",
									 callback_url="https://www.google.com")
		#bot hit
		self.assertEqual(str(groupMeBot.botmanager.getBotByID("dtang_bot_id").name), 'Dorothy Tang ')
		#bot miss
		self.assertIsNone(groupMeBot.botmanager.getBotByID("fister_roboto_id"))

	def test_003_removeBotByName(self):
		groupMeBot.botmanager.addBot(name="Dorothy Tang ",
									 botID="dtang_bot_id",
									 victimID=1234,
									 groupname="Tests",
									 avatar_url="https://www.google.com",
									 callback_url="https://www.google.com")
		#bot hit
		self.assertTrue(groupMeBot.botmanager.removeBotByName("Dorothy Tang "))
		#bot miss
		self.assertFalse(groupMeBot.botmanager.removeBotByName("Fister Roboto"))

	def test_004_removeBotByID(self):
		groupMeBot.botmanager.addBot(name="Dorothy Tang ",
									 botID="dtang_bot_id",
									 victimID=1234,
									 groupname="Tests",
									 avatar_url="https://www.google.com",
									 callback_url="https://www.google.com")
		#bot hit
		self.assertTrue(groupMeBot.botmanager.removeBotByID("dtang_bot_id"))
		#bot miss
		self.assertFalse(groupMeBot.botmanager.removeBotByID("fister_roboto_id"))
	



	

	