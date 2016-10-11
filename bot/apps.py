from django.apps import AppConfig
from django.conf import settings
import os.path

class BotConfig(AppConfig):
    name = 'bot'
    verbose_name = "Ilya's GroupMe Bot"
    def ready(self):
        home_dir = os.path.expanduser("~")
        cred_dir = os.path.join(home_dir, '.groupy.key')
        #write groupy key to app HOME directory sp groupy API can find it 
        with open (cred_dir, 'w') as groupy_key:
            groupy_key.write(settings.GROUPMEBOT_GROUPME_SECRET_KEY)