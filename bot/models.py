from __future__ import unicode_literals
from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class BotManager(models.Manager):
    def getBotByName(self, name):
        try:
            bot = self.get(name=name)
            return bot
        except groupMeBot.DoesNotExist:
            return None

    def getBotByID(self, botID):
        try:
            bot = self.get(botID=botID)
            return bot
        except groupMeBot.DoesNotExist:
            return None

    def addBot(self, name, botID, victimID, groupname, avatar_url, callback_url):
        try:    
            bot = groupMeBot(name = name,
                            botID = botID,
                            victimID = victimID,
                            avatar_url = avatar_url,
                            callback_url = callback_url,
                            groupname = groupname)
            bot.full_clean()
            bot.save()
            return True
        except ValidationError:
            return False

    def removeBotByName(self, name):
        if (self.getBotByName(name) is not None):
            numDeleted = self.getBotByName(name).delete()
            #only ever supposed to delete one bot
            if (numDeleted[0] != 1 or numDeleted[1]['bot.groupMeBot'] != 1):
                return False
            return True
        return False

    def removeBotByID(self, botID):
        if (self.getBotByID(botID) is not None):
            numDeleted = self.getBotByID(botID).delete()
            #only ever supposed to delete one bot
            if (numDeleted[0] != 1 or numDeleted[1]['bot.groupMeBot'] != 1):
                return False
            return True
        return False

#inherits from Model
#id field generated automatically, basically like SQL
class groupMeBot(models.Model):
	botID = models.TextField(unique=True)
	name = models.TextField(unique=True) #shorter than textfield
	victimID = models.IntegerField(unique=True)
	groupname = models.TextField(default="Tests")
	callback_url = models.URLField(default="https://www.google.com", validators=[URLValidator])
	avatar_url = models.URLField(default="https://www.google.com", validators=[URLValidator])

	botmanager = BotManager()

	#__str__ for python 3, __unicode__ for python 2
	def __str__(self):
		return self.name
'''
class groupMeMember(models.Model):
	title = models.CharField(max_length=140) #shorter than textfield 
	body = models.TextField()
	date = models.DateTimeField()
	def __str__(self):
		return self.title
'''

'''
class groupMeGroup(models.Model):
	name = models.TextField(unique=True)  
	groupid = models.TextField()
	
	def __str__(self):
		return self.name
'''