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
from django.views.decorators.csrf import csrf_exempt
client_secret = "6Ld7Fp8dAAAAAJ4kpwVl960_owTUJcqt1ZkRyMnc"
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
# from language_tool_python import LanguageTool as LT
# Create your views here.
urls = [
    #[HREF_LINK,NAME_TO_BE_GIVEN,GRP_ID,SAME_GRP_IN_WEBPAGE,INDI_ID]
    ['/Analyzer/TextAnalyzer/','Text editor',1,'AT',0],
    ['/Analyzer/name_sorting/', 'Words Sorting',1,'AT',1],
    ['/Analyzer/Grammar_correction/','Grammar Corrector',1,'AT',2],
    ['/Analyzer/Online-Keywords-extractor-from-text/','Keyword Extractor',1,'AT',3],
    ['/Analyzer/text-to-base64-converter/','text to base64 encoder',1,'AT',4],
    ['/Analyzer/base64-to-text-converter/','base64 to text decoder',1,'AT',5],
    ['/Analyzer/text-to-image-converter/','text to image converter',1,'AT',6],
    ['/Analyzer/image-to-text-converter/','Image to text converter',1,'AT',7],
    ['/Analyzer/Language-Identifier/','Language Identifier',1,'AT',8],

    ['/Conversion/BinaryConverter/','Binary Converter',2,'CC',0],
    ['/Conversion/DecimalConverter/','Decimal Converter',2,'CC',1],
    ['/Conversion/HexadecimalConverter/','Hexadecimal Converter',2,'CC',2],
    ['/Conversion/CurrencyConverter/','Currency Converter',2,'CC',3],
    [ '/Conversion/infix_to_postfix','Infix to Postfix Converter',2,'CC',4],
    ['/Conversion/infix_to_prefix','Infix to Prefix Converter',2,'CC',5],
    ['/Conversion/postfix_to_infix','Postfix to Infix Converter',2,'CC',6],
    ['/Conversion/prefix_to_postfix','Prefix to Postfix Converter',2,'CC',7],
    ['/Conversion/prefix_to_infix','Prefix to Infix Converter',2,'CC',8],
    ['/Conversion/cgpa_to_percentage/','Cgpa to Percentage Converter',2,'CC',9],
    ['/Conversion/Image_to_base64_Converter/','Image to base64 converter',2,'CC',10],
     ['/Conversion/Base64_to_Image_Converter/','Base64 to Image converter',2,'CC',11],

    ['/Translator/English_to_hindi/','English to Hindi Translator',3,'AT',0],
    ['/Translator/English_to_Marathi/','English to Marathi Translator',3,'AT',1],
    ['/Translator/English_to_German/','English to German Translator',3,'AT',2],
    ['/Translator/English_to_French/','English to French Translator',3,'AT',3],
    ['/Translator/English_to_Arabian/','English to Arabian Translator',3,'AT',4],
    ['/Translator/English_to_spanish/','English to Spanish Translator',3,'AT',5],
    ['/Translator/English_to_thai/','English to Thai Translator',3,'AT',6],

    ['/Calculator/EMI_calculator/','EMI Calculator',4,'CC',0],
    ['/Calculator/GCD_calculator/','GCD Calculator',4,'CC',1],
    ['/Calculator/BMI_calculator/','BMI Calculator',4,'CC',2],
    ['/Calculator/Postfix_calculator/','Postfix Calculator',4,'CC',3],
    ['/Calculator/Prefix_calculator/','Prefix Calculator',4,'CC',4],
    ['/Calculator/Material-weight-calculator/','Material weight Calculator',4,'CC',5],
    

]

def ArrangeSideMapLinksForWebPage(indi_id,grp_id,same_grps_id):
    links_strings_1=[]
    links_strings_2=[]
    for link in range(len(urls)):

        if urls[link][3] == same_grps_id:
            if urls[link][2] == grp_id:
                if urls[link][4]!= indi_id:
                    links_strings_1.append([urls[link][0],urls[link][1]])
                pass
            else:
                links_strings_2.append([urls[link][0],urls[link][1]])
    return links_strings_1,links_strings_2

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
    text=[url for url in urls if url[2]==1]
    converter=[url for url in urls if url[2]==2]
    Translator=[url for url in urls if url[2]==3]
    calculator=[url for url in urls if url[2]==4]

    return render(request,'sitemaps.html',{'text':text,'converter':converter,'translator':Translator,'calculator':calculator})

def text(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(0,1,'AT')
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
        return render(request,'text.html',parms)
    params={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'text.html',params)
def Grammar_correction(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(2,1,'AT')
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
        return render(request,'Grammar_correction.html',param)
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'Grammar_correction.html',param)
        

        

    
#namesorting
def name_sorting(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(1,1,'AT')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'name_sorting.html',param)
#KeywordsExtractionFromText
def KeywordsExtraction(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(3,1,'AT')
    if request.method == "POST":
        text =request.POST['text']
        rake_nltk_var = Rake()
        rake_nltk_var.extract_keywords_from_text(text)
        keyword_extracted = rake_nltk_var.get_ranked_phrases()
        response=json.dumps({'Keyword': keyword_extracted,'keywordLen':len(keyword_extracted)},default=str)
        return HttpResponse(response) 
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'KeywwordsExtraction.html',param)

#text to base64
def texttobase64(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(4,1,'AT')
    if request.method == "POST":
        text =request.POST['text']
        encoded_string = base64.b64encode(text.encode())
        encoded_string = encoded_string.decode()
        response=json.dumps({'Encoded': encoded_string},default=str)
        return HttpResponse(response) 
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'text_to_base64.html',param)

#base64 to text
def base64totext(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(5,1,'AT')
    if request.method == "POST":
        text =request.POST['text']
        decoded_string = base64.b64decode(text.encode())
        decoded_string = decoded_string.decode()
        response=json.dumps({'Decoded': decoded_string},default=str)
        return HttpResponse(response) 
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'base64_to_text.html',param)
#text to image
def texttoimage(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(6,1,'AT')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'texttoimage.html',param)

def texttoimage(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(6,1,'AT')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'texttoimage.html',param)
#image to text
@csrf_exempt
def imagetotext(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(7,1,'AT')
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
            result = pytesseract.image_to_string(img)
        response=json.dumps({'txt': result},default=str)
        return HttpResponse(response)
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'Imagetotext.html',param)

#Language identifier
def LangIdenti(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(8,1,'AT')
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
    return render(request,'LangIdenti.html',param)

#Conversion
def Binaryconversion(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(0,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'Binarycon.html',param)
def Decimalconversion(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(1,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'DecimalCon.html',param)
def Hexadecimalconversion(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(2,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'HexaCon.html',param)
#currency
def Currencyconversion(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(3,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'CurrencyCon.html',param)
def infix_to_postfix(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(4,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'infix_to_postfix.html',param)
#cgpatopercent
def cgpa_to_percentage(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(9,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'cgtopercent.html',param)
##PostfixtoInfix
def postfix_to_infix(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(6,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'postfix_to_infix.html',param)
##Infixtoprefix
def infix_to_prefix(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(5,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'infix_to_prefix.html',param)
##prefixtoPostfix
def prefix_to_postfix(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(7,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'prefix_to_postfix.html',param)
##prefixtoInfix
def prefix_to_infix(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(8,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'prefix_to_infix.html',param)
#Image to base64 converter
@csrf_exempt
def Image_to_base64(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(10,2,'CC')
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
    return render(request,'image_to_base64.html',param)

#Base64 to Image Converter
def Base64_to_Image(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(11,2,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'Base64_to_Image.html',param)

#Translator
def EnglishToHindi(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(0,3,'AT')
    if request.method=='POST':
        text=request.POST.get('text','default')
        trans=Translator()
        
        lang=trans.detect(text)
        t=trans.translate(text,dest='hi')
        alt=True
        param={"ortext":text,"text":t.text,"alt":alt,'link_string1':link_string1,'link_string2':link_string2}
        return render(request,'EnglishToHindi_Transl.html',param)
        # print(text)
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'EnglishToHindi_Transl.html',param)

def EnglishToMarathi(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(1,3,'AT')
    if request.method=="POST":
        text=request.POST.get('text','default')
        trans=Translator()
        
        lang=trans.detect(text)
        t_marathi=trans.translate(text,dest='mr')
    

        alt=True
        param={"ortext":text,"text":t_marathi.text,"alt":alt,'link_string1':link_string1,'link_string2':link_string2}
        return render(request,'EnglishToMarathi_Transl.html',param)
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'EnglishToMarathi_Transl.html',param)
def EnglishToGerman(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(2,3,'AT')
    if request.method=="POST":
        text=request.POST.get('text','default')
        trans=Translator()
        
        lang=trans.detect(text)
        t=trans.translate(text,dest='de')
      

        alt=True
        param={"ortext":text,"text":t.text,"alt":alt,'link_string1':link_string1,'link_string2':link_string2}
        return render(request,'EnglishToGerman_Transl.html',param)
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'EnglishToGerman_Transl.html',param)
def EnglishToFrench(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(3,3,'AT')
    if request.method=="POST":
        text=request.POST.get('text','default')
        trans=Translator()
        
        lang=trans.detect(text)
        t=trans.translate(text,dest='fr')
      

        alt=True
        param={"ortext":text,"text":t.text,"alt":alt,'link_string1':link_string1,'link_string2':link_string2}
        return render(request,'EnglishToFrench_Transl.html',param)
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'EnglishToFrench_Transl.html',param)
def EnglishToArabian(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(4,3,'AT')
    if request.method=="POST":
        text=request.POST.get('text','default')
        trans=Translator()
        
        lang=trans.detect(text)
        t=trans.translate(text,dest='ar')
      

        alt=True
        param={"ortext":text,"text":t.text,"alt":alt,'link_string1':link_string1,'link_string2':link_string2}
        return render(request,'EnglishToArabian_Transl.html',param)
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'EnglishToArabian_Transl.html',param)
def EnglishToSpanish(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(5,3,'AT')
    if request.method=="POST":
        text=request.POST.get('text','default')
        trans=Translator()
        
        lang=trans.detect(text)
        t=trans.translate(text,dest='es')
        alt=True
        param={"ortext":text,"text":t.text,"alt":alt,'link_string1':link_string1,'link_string2':link_string2}
        return render(request,'EnglishToSpanish_Transl.html',param)
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'EnglishToSpanish_Transl.html',param)
def EnglishTothai(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(6,3,'AT')
    if request.method=="POST":
        text=request.POST.get('text','default')
        trans=Translator()
        
        lang=trans.detect(text)
        t=trans.translate(text,dest='th')
        alt=True
        param={"ortext":text,"text":t.text,"alt":alt,'link_string1':link_string1,'link_string2':link_string2}
        return render(request,'EnglishToThai_Transl.html',param)
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'EnglishToThai_Transl.html',param)

#calculator

def Loan_calculator(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(0,4,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'loan_calculator.html',param)
def GCD_calculator(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(1,4,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'GCD_calculator.html',param)
def BMI_calculator(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(2,4,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'BMI_calculator.html',param)
def Postfix_calculator(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(3,4,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'Postfix_calculator.html',param)
def Prefix_calculator(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(4,4,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'Prefix_calculator.html',param)
def material_weight_calculator(request):
    link_string1,link_string2=ArrangeSideMapLinksForWebPage(5,4,'CC')
    param={'link_string1':link_string1,'link_string2':link_string2}
    return render(request,'material_weight_calculator.html',param)
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