from django.shortcuts import render
from datetime import datetime
from ..models import Contact
from basicsite.settings.base import BASE_DIR
import json
import os
import environ

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
client_secret = env('client_secret_captcha')


def isCaptchaValid(r):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    captchaData = {
        'secret': client_secret,
        'response': r,
    }
    import urllib
    data = urllib.parse.urlencode(captchaData).encode()
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    return result['success']


def index(request):
    return render(request, '../templates/index.html')


def ContactMe(request):
    isSub = False
    isValid = False
    if request.method == "POST":
        isSub = True
        name = request.POST.get("name")
        email = request.POST.get("email")

        desc = request.POST.get("desc")
        r = request.POST.get('g-recaptcha-response')
        if isCaptchaValid(r):
            contact = Contact(name=name, email=email,
                              desc=desc, date=datetime.today())
            contact.save()
            isValid = True
        else:
            isValid = False
        return render(request, '../templates/Contact_me.html', {"issub": isSub, "isValid": isValid})
    return render(request, '../templates/Contact_me.html')


def PrivacyPolicy(request):
    return render(request, '../templates/PrivacyPolicy.html')


def Supportme(request):
    return render(request, "../templates/Supportme.html")
