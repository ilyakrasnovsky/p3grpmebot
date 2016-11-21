from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from bot import dbmgr, behavior
from bot.models import groupMeBot

import json
import groupy
import re

def index(request):
	return render(request, 'bot/home.html')

def start_the_fun(request):
	if (request.method == "GET"):
		victimDict = { "victims" : [("11151463", "The Silver Pheasant", "https://i.groupme.com/338bf1100147013161af2ee50beb8cc8"),
                                    ("13565728", "The Silver Pheasant", "https://i.groupme.com/1182x1080.png.d84d67f93a814167a5b27d3e18d61934")]
                    }
		myBehavior = behavior.Behavior()
		myBehavior.releaseTheKraken(victimDict)
	return render(request, 'bot/home.html')			

def end_the_fun(request):
	if (request.method == "GET"):
		myBehavior = behavior.Behavior()
		myBehavior.stowTheKraken()
	return render(request, 'bot/home.html')

def activate_the_fun(request):
	if (request.method == "GET"):
		myBehavior = behavior.Behavior()
		myBehavior.angerTheKraken()
	return render(request, 'bot/home.html')

def deactivate_the_fun(request):
	if (request.method == "GET"):
		myBehavior = behavior.Behavior()
		myBehavior.calmTheKraken()
	return render(request, 'bot/home.html')

@csrf_exempt
def behave(request, victimID):
	#only perform logic if the request was a post
	if (request.method == "POST"):
		myBehavior = behavior.Behavior()
		#parse out HTTP POST request from groupme as json
		json_str = ((request.body).decode('utf-8'))
		jsondata = json.loads(json_str)
		#system_message = {"payload" : "derp" }
		#make sure incoming data is not corrupted
		if ('name' in jsondata):
			#dont operate on GroupMe system messages
			if (jsondata['system'] == True):
				#if the real bot victim changes their name, have the bot adapt
				if (re.search(" changed name to ", jsondata['text']) is not None):
					(oldVictimName, newVictimName) = re.split(" changed name to ", jsondata['text'])
					myBehavior.botAdaptToNameChange(newVictimName, oldVictimName)
				#TODO: IK, if the real bot victim changes their avatar, have the bot adapt
				#bot's change their group name attributes in accordance with a group name change
				if (re.search(" changed the group's name to ", jsondata['text']) is not None):
					newGroupName = re.split(" changed the group's name to ", jsondata['text'])[1]
					for bot in groupMeBot.botmanager.all():
						#TODO: IK, handle bots across multiple groups
						groupMeBot.botmanager.changeBotGroupName(bot.botID, newGroupName)
			else:
				#get the victim
				victim = myBehavior.getVictimByID(victimID)
				#make sure the POSTer was not a bot or the
				#intended victim
				if (myBehavior.getBot(jsondata['name']) is None
					and jsondata['user_id'] != victimID):
					#if bot is active, make the bot behave!
					if (myBehavior.getBotByVictimID(victimID).active == True):
						myBehavior.botBehave(myBehavior.getBotByVictimID(victimID).name, jsondata['text'])
					
		#Save the post to firebase
		#myDbmgr1 = dbmgr.Dbmgr()
		#myDbmgr1.fdb.post("/data/", jsondata)
		#myDbmgr1.fdb.post("/murp/", json.dumps(system_message))
	return render(request, 'bot/home.html')