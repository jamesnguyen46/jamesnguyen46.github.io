from django.shortcuts import render
from profile_project.settings import FIREBASE_DATABASE


def index(request):
    return render(
        request,
        "index.html",
        context={
            "page_icons": FIREBASE_DATABASE.child("page_icons").get().val(),
            "flags": FIREBASE_DATABASE.child("flags").get().val(),
            "profile": FIREBASE_DATABASE.child("profile").get().val(),
            "experience": FIREBASE_DATABASE.child("experience").get().val(),
            "skills": FIREBASE_DATABASE.child("skills").get().val(),
        },
    )
