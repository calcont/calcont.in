from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from basicsite.settings.base import BASE_DIR
import json
import os
import environ
import urllib
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
client_secret = env('client_secret_captcha')


def isCaptchaValid(r):

    url = 'https://www.google.com/recaptcha/api/siteverify'
    captchaData = {
        'secret': client_secret,
        'response': r,
    }
    data = urllib.parse.urlencode(captchaData).encode()
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    return result['success']


def Login(request):
    if request.method == "POST":
        # getting parameters

        usernamelogin = request.POST["usernamelog"]
        passw = request.POST["password"]
        user = authenticate(request, username=usernamelogin, password=passw)
        if user is not None:
            login(request, user)

            messages.success(request, "Successfully login.")

            return redirect('/')
        else:
            messages.warning(request, "Invalid Credentials.")

            return render(request, "../templates/Login.html")

    if request.user.is_authenticated:
        return HttpResponse("400 bad request")

    return render(request, "../templates/Login.html")


def Signin(request):
    isSub = False
    isValid = False
    if request.method == "POST":
        # getting parameters
        isSub = True
        username = request.POST["username"]
        email = request.POST["emailsign"]
        pass1 = request.POST["password1"]
        r = request.POST.get('g-recaptcha-response')
        if username in User.objects.filter(is_active=True).values_list('username', flat=True):

            messages.warning(
                request, "Username is already taken!Please try with other username.")

            return render(request, "../templates/Signin.html")

        x = User.objects.filter(is_active=True).values_list('email', flat=True)
        if email in x:

            messages.warning(
                request, "Email Exist!Please try with other  email.")

            return render(request, "../templates/Signin.html")

        # create user

        if len(pass1) < 5 or len(pass1) > 18 or not pass1.isalnum():
            messages.warning(request, "Invalid Password.")
            return render(request, "../templates/Signin.html")

        if isCaptchaValid(r):
            myuser = User.objects.create_user(username, email, pass1)
            myuser.save()
            messages.success(request, "Accout has been created successfully")
            isValid = True
            return render(request, "../templates/index.html", {"canlogin": True})
        else:
            isValid = False
            return render(request, "../templates/Signin.html", {"issub": isSub, "isValid": isValid})

        # return render(request,"index.html",param)
    if request.user.is_authenticated:
        return HttpResponse("400 bad request")
    return render(request, "../templates/Signin.html")


def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out successfully")
        return redirect("/")
