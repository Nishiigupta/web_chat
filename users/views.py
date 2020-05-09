from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth import authenticate, login, logout


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html', {"message": None})
    context = {
        "message": "Welcome to our chatting app"
    }
    return render(request, "users/index.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "users/login.html", {"message": "Invalid crediatials"})

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "logged out"})