'''
Sets up secret keys for developing our 
application locally on your machine. Run:

$ python localcreds.py '<GROUPMEBOT_DJANGO_SECRET_KEY>' '<GROUPMEBOT_FIREBASE_SECRET_KEY>' '<GROUPMEBOT_GROUPME_SECRET_KEY> '<GROUPMEBOT_POSTGRES_SECRET_KEY>'

to set it up (NOTE THE QUOTES!). This only needs to be done once.
'''
import os, sys

def get_credentials(key=None, django=False, groupme=False, firebase=False, postgres=False):
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
    elif(django):
        credential_path = os.path.join(credential_dir,
                                   'GROUPMEBOT_DJANGO_SECRET_KEY.txt')
    elif(postgres):
        credential_path = os.path.join(credential_dir,
                                   'GROUPMEBOT_POSTGRES_SECRET_KEY.txt')
    if (key != None):
        with open (credential_path, 'w') as secret_file:
            secret_file.write(key)    
    with open (credential_path, 'r') as secret_file:
        SECRET_KEY = secret_file.read()
    return SECRET_KEY

#Tester client
def main(argv):
    if (len(argv) >= 4):
        GROUPMEBOT_DJANGO_SECRET_KEY = argv[0]
        GROUPMEBOT_FIREBASE_SECRET_KEY = argv[1]
        GROUPMEBOT_GROUPME_SECRET_KEY = argv[2]
        GROUPMEBOT_POSTGRES_SECRET_KEY = argv[3]
    else:
        GROUPMEBOT_DJANGO_SECRET_KEY = None
        GROUPMEBOT_FIREBASE_SECRET_KEY = None
        GROUPMEBOT_GROUPME_SECRET_KEY = None
        GROUPMEBOT_POSTGRES_SECRET_KEY = None
    print ("GROUPMEBOT_DJANGO_SECRET_KEY SET TO  : " + get_credentials(GROUPMEBOT_DJANGO_SECRET_KEY, django=True))
    print ("GROUPMEBOT_FIREBASE_SECRET_KEY SET TO  : " + get_credentials(GROUPMEBOT_FIREBASE_SECRET_KEY, firebase=True))
    print ('GROUPMEBOT_GROUPME_SECRET_KEY SET TO : ' + get_credentials(GROUPMEBOT_GROUPME_SECRET_KEY, groupme=True))
    print ('GROUPMEBOT_POSTGRES_SECRET_KEY SET TO : ' + get_credentials(GROUPMEBOT_POSTGRES_SECRET_KEY, postgres=True))

if __name__ == '__main__':
    main(sys.argv[1:])