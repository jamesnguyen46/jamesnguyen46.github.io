import os
import json
import pyrebase

json_str=os.environ.get('FIREBASE_CONFIG')
config = json.loads(json_str)
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()