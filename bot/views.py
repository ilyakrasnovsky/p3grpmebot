from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
#from django.views import View
#from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from bot import dbmgr #, behavior
import json
import groupy

def index(request):
	return render(request, 'bot/home.html')

@csrf_exempt
def boobot(request):
	#only perform logic if the request was a post
	if (request.method == "POST"):
		#parse out HTTP POST request from groupme as json
		json_str = ((request.body).decode('utf-8'))
		jsondata = json.loads(json_str)
		
		'''
		#make sure incoming data is not corrupted
		if ('name' in jsondata):
			#if the real bot victim changes their name, have the
			#bot adapt
			if (jsondata['name'] == "GroupMe"):
				pass

			#make sure the POSTer was not a bot or the
			#intended victim, or groupMe admin
			if (jsondata['name'] != "Haiti Badding Sr " and 
				jsondata['name'] != "Haiti Badding Sr" and
				jsondata['name'] != "GroupMe"):
				#get relevant bots using groupy API
				hannah_bot = behavior.getBot("Haiti Badding Sr ")
				if (hannah_bot is not None):
					hannah_bot.post("Hi! I'm Hannah!")
		'''
			
		#Save the post to my database
		dbmgr1 = dbmgr.Dbmgr()
		dbmgr1.fdb.post("/data/", jsondata)
		
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