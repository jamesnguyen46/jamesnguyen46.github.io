from django.shortcuts import render
from resume.firebase import database

def index(request):
    first_name = database.child('data').child('profile').child('first_name').get().val()
    last_name = database.child('data').child('profile').child('last_name').get().val()

    context = {
        'first_name':first_name,
        'last_name':last_name
    }
    return render(request, 'index.html', context)
