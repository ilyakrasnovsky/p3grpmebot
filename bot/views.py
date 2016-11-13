from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from bot import dbmgr, behavior

import json
import groupy
import re

def index(request):
	return render(request, 'bot/home.html')

@csrf_exempt
def boobot_ilya(request):
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
			else:
				#make sure the POSTer was not a bot or the
				#intended victim
				if (myBehavior.getBot(jsondata['name']) is None
					and jsondata['name'] != "Ilya Krasnovsky"):
					#make the bot behave!
					bot = myBehavior.botBehave("Ilya Krasnovsky ", jsondata['text'])
				
		#Save the post to firebase
		#myDbmgr1 = dbmgr.Dbmgr()
		#myDbmgr1.fdb.post("/data/", jsondata)
		#myDbmgr1.fdb.post("/murp/", json.dumps(system_message))

	return render(request, 'bot/home.html')

@csrf_exempt
def boobot_dorothy(request):
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
			else:
				#make sure the POSTer was not a bot or the
				#intended victim
				if (myBehavior.getBot(jsondata['name']) is None
					and jsondata['name'] != "Dorothy Tang"): #todo, this cant be hardcoded
					#make the bot behave!
					bot = myBehavior.botBehave("Dorothy Tang ", jsondata['text'])
					
		#Save the post to firebase
		#myDbmgr1 = dbmgr.Dbmgr()
		#myDbmgr1.fdb.post("/data/", jsondata)
		#myDbmgr1.fdb.post("/murp/", json.dumps(system_message))

	return render(request, 'bot/home.html')

def start_the_fun(request):
	if (request.method == "GET"):
		myBehavior = behavior.Behavior()
		myBehavior.releaseTheKraken()
	return render(request, 'bot/home.html')			

def end_the_fun(request):
	if (request.method == "GET"):
		myBehavior = behavior.Behavior()
		myBehavior.stowTheKraken()
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
			else:
				#get the victim
				victim = myBehavior.getVictimByID(victimID)
				#make sure the POSTer was not a bot or the
				#intended victim
				if (myBehavior.getBot(jsondata['name']) is None
					and jsondata['name'] != victim.identification()['nickname']):
					#make the bot behave!
					bot = myBehavior.botBehave(victim.identification()['nickname'] + " ", jsondata['text'])
					
		#Save the post to firebase
		#myDbmgr1 = dbmgr.Dbmgr()
		#myDbmgr1.fdb.post("/data/", jsondata)
		#myDbmgr1.fdb.post("/murp/", json.dumps(system_message))
	return render(request, 'bot/home.html')


'''
class: Bot

description:
    - Bot class, inherits from Django View

attributes:
    name : bot's name (string)
    id : bot's groupme id (string)    

initializer input:
    name, id

functions:
	get() - NOT USED
	post()
	perform()
'''
'''
class Bot(View):
    def __init__(self, botname, botid):
        self.botname = botname
        self.botid = botid

    #def get(self, request):
    #	return HttpResponse("lolget")

	def post(self, request):
		self.perform()
    	return HttpResponse("lolpost")

    def perform(self):
    	print ("lol, i've performed")
'''