from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
#from django.views import View
#from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from . import dbmgr
import json
#import groupy

def index(request):
	return render(request, 'bot/home.html')

@csrf_exempt
def boobot(request):
	dbmgr1 = dbmgr.Dbmgr()
	#wahbot = getBot("wah")	
	if (request.method == "POST"):
		#print (json.loads(request.body))
		json_str = ((request.body).decode('utf-8'))
		jsondata = json.loads(json_str)
		#print (request.body)
		#print (request.POST.dict())
		#dbmgr1.fdb.post("/lewl/", request.POST.dict())
		dbmgr1.addMessage(jsondata['name'], jsondata['text'])
	return render(request, 'bot/home.html')


'''
def getBot(botname):
	for mybot in groupy.Bot.list():
		if (mybot.name == botname):
			print ("found bot!")
			return mybot
'''

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