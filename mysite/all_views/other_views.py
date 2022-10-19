from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
import json
from datetime import datetime
from .. import MyFunctions
from .. import globals
from ..models import Contact
client_secret = "6Ld7Fp8dAAAAAJ4kpwVl960_owTUJcqt1ZkRyMnc"


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

def sitemaps(request):
    text = [url for url in globals.urlSideMapList() if url[2] == 1]
    converter = [url for url in globals.urlSideMapList() if url[2] == 2]
    Translator = [url for url in globals.urlSideMapList() if url[2] == 3]
    calculator = [url for url in globals.urlSideMapList() if url[2] == 4]

    return render(request, 'sitemaps.html', {'text': text, 'converter': converter, 'translator': Translator, 'calculator': calculator})

# contact
def ContactMe(request):
    isSub = False
    isValid = False
    if request.method == "POST":
        isSub = True
        name = request.POST.get("name")
        email = request.POST.get("email")

        desc = request.POST.get("desc")
        r = request.POST.get('g-recaptcha-response')
        import joblib
        models = joblib.load(f'spam.pkl')
        v = joblib.load(f'vector.pickel')
        spam = models.predict(v.transform([desc]))
        if spam[0] == 0:
            pass
        else:
            desc = "[spam] " + desc
        if isCaptchaValid(r):
            contact = Contact(name=name, email=email,
                              desc=desc, date=datetime.today())
            contact.save()
            isValid = True
        else:
            than = 'notdone'
            isValid = False
        return render(request, '../templates/Contact_me.html', {"issub": isSub, "isValid": isValid})
    return render(request, '../templates/Contact_me.html')


def Aboutme(request):
    return render(request, '../templates/Aboutme.html')


def PrivacyPolicy(request):
    return render(request, '../templates/PrivacyPolicy.html')
# authentication

def Supportme(request):
    return render(request, "../templates/Supportme.html")