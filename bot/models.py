from __future__ import unicode_literals
from django.db import models

#inherits from Model
#id field generated automatically, basically like SQL
class groupMeBot(models.Model):
	botid = models.TextField(unique=True)
	name = models.TextField(unique=True) #shorter than textfield
	callback_url = models.URLField()
	avatar_url = models.URLField()

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

class groupMeGroup(models.Model):
	title = models.CharField(max_length=140) #shorter than textfield 
	body = models.TextField()
	date = models.DateTimeField()
	
	def __str__(self):
		return self.title
'''