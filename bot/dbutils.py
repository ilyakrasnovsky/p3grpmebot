'''
module : dbutils

contains classes/functions for various database related
utilities, like making sure attributes add up to 20, stuff
like that

classes:

functions:
	is_integer()
	is_number()
	is_valid() --> this is temporary

'''

#Function takes in s, and determines if it
#is a float (returns True if yes, False if no)
def is_number(s):
    try:
        float(s)
        return (True)
    except ValueError:
        return False
    except TypeError:
        return False

#Function takes in s, and determines if it
#is an integer (returns True if yes, False if no)
def is_integer(s):
    try:
        int(s)
        return (True)
    except ValueError:
        return False
    except TypeError:
        return False

def is_valid(s):
	pass