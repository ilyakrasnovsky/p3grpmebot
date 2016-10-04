'''
Sets up secret keys for developing our 
application locally on your machine. Run:

$ python localcreds.py '<GROUPMEBOT_DJANGO_SECRET_KEY>' '<GROUPMEBOT_FIREBASE_SECRET_KEY>' '<GROUPMEBOT_GROUPME_SECRET_KEY>'

to set it up (NOTE THE QUOTES!). This only needs to be done once.
'''
import os, sys

def get_credentials(key=None, groupme=False, firebase=False):
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    if (groupme):
        credential_path = os.path.join(credential_dir,
                                   'GROUPMEBOT_GROUPME_SECRET_KEY.txt')
    elif (firebase):
        credential_path = os.path.join(credential_dir,
                                   'GROUPMEBOT_FIREBASE_SECRET_KEY.txt')
    else:
        credential_path = os.path.join(credential_dir,
                                   'GROUPMEBOT_DJANGO_SECRET_KEY.txt')
    if (key != None):
        with open (credential_path, 'w') as secret_file:
            secret_file.write(key)    
    with open (credential_path, 'r') as secret_file:
        SECRET_KEY = secret_file.read()
    return SECRET_KEY

#Tester client
def main(argv):
    if (len(argv) >= 3):
        GROUPMEBOT_DJANGO_SECRET_KEY = argv[0]
        GROUPMEBOT_FIREBASE_SECRET_KEY = argv[1]
        GROUPMEBOT_GROUPME_SECRET_KEY = argv[2]
    else:
        GROUPMEBOT_DJANGO_SECRET_KEY = None
        GROUPMEBOT_FIREBASE_SECRET_KEY = None
        GROUPMEBOT_GROUPME_SECRET_KEY = None
    print ("GROUPMEBOT_DJANGO_SECRET_KEY SET TO  : " + get_credentials(GROUPMEBOT_DJANGO_SECRET_KEY))
    print ("GROUPMEBOT_FIREBASE_SECRET_KEY SET TO  : " + get_credentials(GROUPMEBOT_FIREBASE_SECRET_KEY, firebase=True))
    print ('GROUPMEBOT_GROUPME_SECRET_KEY SET TO : ' + get_credentials(GROUPMEBOT_GROUPME_SECRET_KEY, groupme=True))

if __name__ == '__main__':
    main(sys.argv[1:])