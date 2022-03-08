import googletrans
import speech_recognition as sr  
from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from .models import Headlines,Contact,Donate
from googletrans import Translator
from rake_nltk import Rake
import speech_recognition as sr
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import os
import math
import random
import smtplib
import base64
from PIL import Image, ImageDraw
import pytesseract
from io import BytesIO
import json
import joblib
from . import MyFunctions
from . import globals
from django.views.decorators.csrf import csrf_exempt
client_secret = "6Ld7Fp8dAAAAAJ4kpwVl960_owTUJcqt1ZkRyMnc"
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
tran = MyFunctions.TranslatorFun()
SideMap = MyFunctions.ArrangeSideMapForWebpage()
# from language_tool_python import LanguageTool as LT
# Create your views here.

def isCaptchaValid(r):
    
    url = 'https://www.google.com/recaptcha/api/siteverify'
    captchaData = {
        'secret': client_secret,
        'response': r,
    }
    import urllib
    data = urllib.parse.urlencode(captchaData).encode()
    req = urllib.request.Request(url,data = data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    return result['success']

def index(request):
    return render(request,'index.html')
    
def error_404(request , exception):
    return render(request,'404.html',status=404)

def error_500(request):
    return render(request,'500.html' ,status=500)
#Analyzer
def sitemaps(request):
    text=[url for url in globals.urlSideMapList() if url[2]==1]
    converter=[url for url in globals.urlSideMapList() if url[2]==2]
    Translator=[url for url in globals.urlSideMapList() if url[2]==3]
    calculator=[url for url in globals.urlSideMapList() if url[2]==4]

    return render(request,'sitemaps.html',{'text':text,'converter':converter,'translator':Translator,'calculator':calculator})

def text(request):
    link_string1,link_string2=SideMap.arrange(0,1,'AT')
    if request.method=="POST":
        tex=request.POST.get('text','default')
        removepunc=request.POST.get('removepunc','off')
        fullcaps=request.POST.get('fullcaps','off')
        newlineremover=request.POST.get('newlineremover','off')
        xtraspaceremover=request.POST.get('xtraspaceremover','off')
        # print(tex)
        IsEnter=True
        if removepunc=='on':
            pun='''!.()-[]{};:'"/\,<>?@#$%^_~'''
            analysed=""
            for char in tex:
                if char not in pun:
                    analysed= analysed + char
            
            text=analysed
        if fullcaps=='on':
            analysed=tex.upper()
            
            text=analysed
        if newlineremover=="on":
            analysed=""
            for char in tex:
                if char!='\n' and char!='\r':
                    analysed+=char
            
            text=analysed
        if xtraspaceremover=="on":
            analysed=""
            for i,char in enumerate(tex):
                if not(tex[i]==" "):
                    analysed+=char
            
            text=analysed
        
        if  fullcaps!='on' and removepunc!="on" and xtraspaceremover!="on" and newlineremover!="on":
            
            analysed="PLEASE SELECT OPERATION."
        if tex=="":
            analysed="PLEASE ENTER TEXT FIRST."

        
        parms={'Text':analysed,'IsEnter':IsEnter,'OrText':tex,'link_string1':link_string1,'link_string2':link_string2}
        return render(request,'textAnalyzer/text.html',parms)
    params={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'textAnalyzer/text.html',params)
def Grammar_correction(request):
    link_string1,link_string2=SideMap.arrange(2,1,'AT')
    if request.method=='POST':
        IsEnter=True
        text=request.POST.get('text','default')
        from gingerit.gingerit import GingerIt
        length_text=len(text)
        if length_text<300:
            result = GingerIt().parse(text)
            n=len(list(result['corrections']))
            d=[]
            a=[]
            for i in range(n):
                dash=list(result['corrections'][i].items())
                d.append(dash[0][1])
            d.reverse()
            i=0
            while i<(len(text)):
                if i in d: 
                    for j in range(i,len(text)):
                        if text[j]==" ":
                            break
                    a.append("\u0332".join(text[i:j+1]))
                    # print("\u0332".join(text[i]))
                    i=j
                else:
                    a.append(text[i])
                i+=1 
            Text=""
            for i in a:
                Text+=i


            param={'NewText':result['result'],"text":Text,"IsEnter":IsEnter,"length_text":length_text,'link_string1':link_string1,'link_string2':link_string2}
        else:
            param={'NewText':" ","text":text,"IsEnter":IsEnter,"length_text":length_text,'link_string1':link_string1,'link_string2':link_string2}
        return render(request,'textAnalyzer/Grammar_correction.html',param)
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'textAnalyzer/Grammar_correction.html',param)
#namesorting
def name_sorting(request):
    link_string1,link_string2=SideMap.arrange(1,1,'AT')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'textAnalyzer/name_sorting.html',param)

#KeywordsExtractionFromText
def KeywordsExtraction(request):
    link_string1,link_string2=SideMap.arrange(3,1,'AT')
    if request.method == "POST":
        text =request.POST['text']
        rake_nltk_var = Rake()
        rake_nltk_var.extract_keywords_from_text(text)
        keyword_extracted = rake_nltk_var.get_ranked_phrases()
        response=json.dumps({'Keyword': keyword_extracted,'keywordLen':len(keyword_extracted)},default=str)
        return HttpResponse(response) 
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'textAnalyzer/KeywwordsExtraction.html',param)

#text to base64
def texttobase64(request):
    link_string1,link_string2=SideMap.arrange(4,1,'AT')
    if request.method == "POST":
        text =request.POST['text']
        encoded_string = base64.b64encode(text.encode())
        encoded_string = encoded_string.decode()
        response=json.dumps({'Encoded': encoded_string},default=str)
        return HttpResponse(response) 
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'textAnalyzer/text_to_base64.html',param)

#base64 to text
def base64totext(request):
    link_string1,link_string2=SideMap.arrange(5,1,'AT')
    if request.method == "POST":
        text =request.POST['text']
        decoded_string = base64.b64decode(text.encode())
        decoded_string = decoded_string.decode()
        response=json.dumps({'Decoded': decoded_string},default=str)
        return HttpResponse(response) 
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'textAnalyzer/base64_to_text.html',param)

#texttoimage
def texttoimage(request):
    link_string1,link_string2=SideMap.arrange(6,1,'AT')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'textAnalyzer/texttoimage.html',param)

@csrf_exempt
def imagetotext(request):
    link_string1,link_string2=SideMap.arrange(7,1,'AT')
    if request.method == "POST":
        # if request.POST['isurl']=="1":
        
        # print(request.FILES)
        try: 
            image =request.FILES['image']
            img = Image.open(image)
               
            result = pytesseract.image_to_string(img)
        except:
            
            url = request.POST.get('url')
            import requests
            response = requests.get(url)
            img = Image.open(BytesIO(response.content)) 
            print(img)
            result = pytesseract.image_to_string(img)
        response=json.dumps({'txt': result},default=str)
        return HttpResponse(response)
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'textAnalyzer/Imagetotext.html',param)

#Language identifier
def LangIdenti(request):
    link_string1,link_string2=SideMap.arrange(8,1,'AT')
    from googletrans import Translator
    t = Translator()
    if request.method == "POST":
        text =request.POST['text']
        if request.POST.get('isDetect')=="0":
            eng_txt= t.translate(text, dest='en')
            response=json.dumps({'e_lang': eng_txt.text},default=str)
            return HttpResponse(response)
        else:
            lang = t.detect(text)
            try:
                response=json.dumps({'lang': googletrans.LANGUAGES[lang.lang]},default=str)
            except:
                err = "Not able to detect this language"
                response=json.dumps({'lang': err},default=str)
            return HttpResponse(response)
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'textAnalyzer/LangIdenti.html',param)


#Conversion
def Binaryconversion(request):
    link_string1,link_string2=SideMap.arrange(0,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'converter/Binarycon.html',param)
def Decimalconversion(request):
    link_string1,link_string2=SideMap.arrange(1,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'converter/DecimalCon.html',param)
def Hexadecimalconversion(request):
    link_string1,link_string2=SideMap.arrange(2,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'converter/HexaCon.html',param)
#currency
def Currencyconversion(request):
    link_string1,link_string2=SideMap.arrange(3,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'converter/CurrencyCon.html',param)
def infix_to_postfix(request):
    link_string1,link_string2=SideMap.arrange(4,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'converter/infix_to_postfix.html',param)
#cgpatopercent
def cgpa_to_percentage(request):
    link_string1,link_string2=SideMap.arrange(9,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'converter/cgtopercent.html',param)
##PostfixtoInfix
def postfix_to_infix(request):
    link_string1,link_string2=SideMap.arrange(6,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'converter/postfix_to_infix.html',param)
##Infixtoprefix
def infix_to_prefix(request):
    link_string1,link_string2=SideMap.arrange(5,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'converter/infix_to_prefix.html',param)
##prefixtoPostfix
def prefix_to_postfix(request):
    link_string1,link_string2=SideMap.arrange(7,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'converter/prefix_to_postfix.html',param)
##prefixtoInfix
def prefix_to_infix(request):
    link_string1,link_string2=SideMap.arrange(8,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'converter/prefix_to_infix.html',param)
##prefixtoInfix
def prefix_to_infix(request):
    link_string1,link_string2=SideMap.arrange(8,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'converter/prefix_to_infix.html',param)

#Image to base64 converter
@csrf_exempt
def Image_to_base64(request):
    link_string1,link_string2=SideMap.arrange(10,2,'CC')
    if request.method == "POST":
        try: 
            image =request.FILES['image']
            encoded_string = base64.b64encode(image.read())
        except:
            url = request.POST.get('url')
            import requests
            response = requests.get(url)
            encoded_string = base64.b64encode(response.content)
        response=json.dumps({'txt': encoded_string.decode()},default=str)
        return HttpResponse(response)
        
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'converter/image_to_base64.html',param)

#Base64 to Image Converter
def Base64_to_Image(request):
    link_string1,link_string2=SideMap.arrange(11,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'converter/Base64_to_Image.html',param)


#Translator
def EnglishToHindi(request):
    respons = tran.EnglishToOther(request,0,'hi','Translator/EnglishToOther/EnglishToHindi_Transl.html')
    return respons
def EnglishToMarathi(request):
    respons = tran.EnglishToOther(request,1,'mr','Translator/EnglishToOther/EnglishToMarathi_Transl.html')
    return respons
def EnglishToGerman(request):
    respons = tran.EnglishToOther(request,2,'de','Translator/EnglishToOther/EnglishToGerman_Transl.html')
    return respons
def EnglishToFrench(request):
    respons = tran.EnglishToOther(request,3,'fr','Translator/EnglishToOther/EnglishToFrench_Transl.html')
    return respons
def EnglishToArabian(request):
    respons = tran.EnglishToOther(request,4,'ar','Translator/EnglishToOther/EnglishToArabian_Transl.html')
    return respons
def EnglishToSpanish(request):
    respons = tran.EnglishToOther(request,5,'es','Translator/EnglishToOther/EnglishToSpanish_Transl.html')
    return respons
def EnglishTothai(request):
    respons = tran.EnglishToOther(request,6,'th','Translator/EnglishToOther/EnglishToThai_Transl.html')
    return respons

##hindi.to english
def HindiToEnglish(request):
    respons = tran.HindiToOther(request,7,'en','hi','Translator/HindiToOther/HindiToEnglish_Transl.html')
    return respons
def HindiToMarathi(request):
    respons = tran.HindiToOther(request,8,'mr','hi','Translator/HindiToOther/HindiToMarathi_Transl.html')
    return respons
def HindiToGerman(request):
    respons = tran.HindiToOther(request,9,'de','hi','Translator/HindiToOther/HindiToGerman_Transl.html')
    return respons
def HindiToFrench(request):
    respons = tran.HindiToOther(request,10,'fr','hi','Translator/HindiToOther/HindiToFrench_Transl.html')
    return respons
def HindiToArabian(request):
    respons = tran.HindiToOther(request,11,'ar','hi','Translator/HindiToOther/HindiToArabian_Transl.html')
    return respons
def HindiToSpanish(request):
    respons = tran.HindiToOther(request,12,'es','hi','Translator/HindiToOther/HindiToSpanish_Transl.html')
    return respons
def HindiToThai(request):
    respons = tran.HindiToOther(request,13,'th','hi','Translator/HindiToOther/HindiToThai_Transl.html')
    return respons


#calculator

def Loan_calculator(request):
    link_string1,link_string2=SideMap.arrange(0,4,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'calculator/loan_calculator.html',param)
def GCD_calculator(request):
    link_string1,link_string2=SideMap.arrange(1,4,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'calculator/GCD_calculator.html',param)
def BMI_calculator(request):
    link_string1,link_string2=SideMap.arrange(2,4,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'calculator/BMI_calculator.html',param)
def Postfix_calculator(request):
    link_string1,link_string2=SideMap.arrange(3,4,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'calculator/Postfix_calculator.html',param)
def Prefix_calculator(request):
    link_string1,link_string2=SideMap.arrange(4,4,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'calculator/Prefix_calculator.html',param)
def material_weight_calculator(request):
    link_string1,link_string2=SideMap.arrange(5,4,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'calculator/material_weight_calculator.html',param)
#contact
def ContactMe(request):
    isSub=False
    isValid=False
    if request.method == "POST":
        isSub=True
        name=request.POST.get("name")
        email=request.POST.get("email")
   
        desc=request.POST.get("desc")
        r = request.POST.get('g-recaptcha-response')
        import joblib
        models = joblib.load(f'spam.pkl')
        v = joblib.load(f'vector.pickel')
        spam = models.predict(v.transform([desc]))
        if spam[0]==0:
            pass
        else:
            desc = "[spam] " + desc
        if isCaptchaValid(r):
            contact=Contact(name=name,email=email,desc=desc,date=datetime.today())
            contact.save()
            isValid=True
        else:
            than = 'notdone'
            isValid=False
        return render(request,'Contact_me.html',{"issub":isSub,"isValid":isValid})
    return render(request,'Contact_me.html')
def Aboutme(request):
    return render(request,'Aboutme.html')
def PrivacyPolicy(request):
    return render(request,'PrivacyPolicy.html')
#authentication
def Login(request):
    if request.method == "POST":
        #getting parameters
       
        usernamelogin=request.POST["usernamelog"]
        passw=request.POST["password"]
        user=authenticate(request,username=usernamelogin,password=passw)
        if user is not None:
            login(request,user)
            
            
            messages.success(request,"Successfully login.")
            Login=True
            
            return redirect('/')
        else:
            messages.warning(request,"Invalid Credentials.")
            
            return render(request, "Login.html")
            
    if request.user.is_authenticated:
        return HttpResponse("400 bad request")    
    
    return render(request, "Login.html")
def Signin(request):
    isSub=False
    isValid=False
    if request.method == "POST":
        #getting parameters
        isSub = True
        username=request.POST["username"]        
        email=request.POST["emailsign"]
        pass1=request.POST["password1"]
        r = request.POST.get('g-recaptcha-response')
        if username in User.objects.filter(is_active=True).values_list('username',flat=True):

            messages.warning(request,"Username is already taken!Please try with other username.")
            
            return render(request,"Signin.html")
        
     
        x=User.objects.filter(is_active=True).values_list('email',flat=True)
        if email  in x :
            
            messages.warning(request,"Email Exist!Please try with other  email.")
            
            return render(request,"Signin.html")
        
        #create user
       
           
        if len(pass1)<5 or len(pass1)>10 or not pass1.isalnum():
            messages.warning(request,"Invalid Password.")
            return render(request,"Signin.html")


        if isCaptchaValid(r):
            myuser=User.objects.create_user(username,email,pass1)
            myuser.save()
            messages.success(request,"Accout has been created successfully")
            isValid=True
            return render(request,"index.html",{"canlogin":True})
        else:
            isValid=False
            return render(request,"Signin.html",{"issub":isSub,"isValid":isValid})
        
        
     
        
        # return render(request,"index.html",param)
    if request.user.is_authenticated:
        return HttpResponse("400 bad request")  
    return render(request,"Signin.html")
def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out successfully")
        return redirect("/")
def Supportme(request):
    return render(request,"Supportme.html")