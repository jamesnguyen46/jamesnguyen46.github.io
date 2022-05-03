from os import environ as env
import pyrebase

config = {
  "apiKey": env.get('FIREBASE_API_KEY'),
  "authDomain": env.get('FIREBASE_AUTH_DOMAIN'),
  "databaseURL": env.get('FIREBASE_DATABASE_URL'),
  "storageBucket": env.get('FIREBASE_STORAGE_BUCKET')
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()