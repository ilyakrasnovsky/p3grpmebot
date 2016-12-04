from cleverbot import Cleverbot
try:
	cb = Cleverbot()
	print (cb.ask("hohoho"))
except IndexError:
	print ("cleverbot API is being annoying")