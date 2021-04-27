import speech_recognition as sr  
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .models import Headlines,Contact
from googletrans import Translator
import speech_recognition as sr
# from language_tool_python import LanguageTool as LT
# Create your views here.
#username Amar pass:Amar123
def index(request):
    # title=Headlines.objects.all()
    # Text=Headlines.objects.values('text')
    # # print(title)
    # # print(text)
    # n=len(title)
    # alltitle=[]
    # alltitle.append([Text,n])
    # params={"ALL":alltitle}
    # print(n)
    # print(params)
    return render(request,'index.html')
#Analyzer

def text(request):
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

        
        parms={'Text':analysed,'IsEnter':IsEnter,'OrText':tex}
        return render(request,'text.html',parms)
    return render(request,'text.html')
def Grammar_correction(request):
    
    if request.method=='POST':
        IsEnter=True
        text=request.POST.get('text','default')
        
        from gingerit.gingerit import GingerIt
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



        param={'NewText':result['result'],"text":Text,"IsEnter":IsEnter}
        
        return render(request,'Grammar_correction.html',param)
    return render(request,'Grammar_correction.html')
        

        

    
#namesorting
def name_sorting(request):
    return render(request,'name_sorting.html')
#Conversion
def Binaryconversion(request):
    return render(request,'Binarycon.html')
def Decimalconversion(request):
    return render(request,'DecimalCon.html')
def Hexadecimalconversion(request):
    return render(request,'HexaCon.html')
def cgpa_to_percentage(request):
    return render(request,'DecimalCon.html')
def Unitconversion(request):
    return render(request,'UnitCon.html')
#metr
def Unit_mtocm_conversion(request):
    return render(request,'UnitCon_mtocm.html')
def Unit_mtomm_conversion(request):
    return render(request,'UnitCon_mtomm.html')
def Unit_mtoinch_conversion(request):
    return render(request,'UnitCon_mtoinch.html')
def Unit_mtomile_conversion(request):
    return render(request,'UnitCon_mtomile.html')
def Unit_mtofoot_conversion(request):
    return render(request,'UnitCon_mtofoot.html')
def Unit_mtoyard_conversion(request):
    return render(request,'UnitCon_mtoyard.html')
def Unit_mtoangstrom_conversion(request):
    return render(request,'UnitCon_mtoangstrom.html')
#cm
def Unit_cmtomm_conversion(request):
    return render(request,'UnitCon_cmtomm.html')
def Unit_cmtoinch_conversion(request):
    return render(request,'UnitCon_cmtoinch.html')
def Unit_cmtomile_conversion(request):
    return render(request,'UnitCon_cmtomile.html')
def Unit_cmtofoot_conversion(request):
    return render(request,'UnitCon_cmtofoot.html')
def Unit_cmtoyard_conversion(request):
    return render(request,'UnitCon_cmtoyard.html')
def Unit_cmtoangstrom_conversion(request):
    return render(request,'UnitCon_cmtoangstrom.html')
#currency
def Currencyconversion(request):
    return render(request,'CurrencyCon.html')
def infix_to_postfix(request):
    return render(request,'infix_to_postfix.html')
def Language_Translator(request):
    return render(request,'Language_Translator.html')


#Translator
def EnglishToHindi(request):
    if request.method=='POST':

    
    
        text=request.POST.get('text','default')
        trans=Translator()
        
        lang=trans.detect(text)
        t=trans.translate(text,dest='hi')
      

        alt=True
        param={"ortext":text,"text":t.text,"alt":alt}
        return render(request,'EnglishToHindi_Transl.html',param)
        # print(text)
    return render(request,'EnglishToHindi_Transl.html')
# def voice_recognition(request):
#     data = request.POST.get('data')
#     if int(data)==0:

#         print(data)
# # get audio from the microphone                                                                       
#         r = sr.Recognizer()                                                                                   
#         with sr.Microphone() as source:                                                                       
                                                                                              
#             audio = r.listen(source)   

#         try:
#             reply= r.recognize_google(audio)
#             success=True
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#             success=False
#             reply="Could not understand audio"
#         except sr.RequestError as e:
#             reply="Could not request results; {0}".format(e)
        
#         params={"recognize":reply,"done":success}
#         print(params)
#         return render(request,'EnglishToHindi_Transl.html',params)
        
#     return render(request,'EnglishToHindi_Transl.html')    
def EnglishToMarathi(request):
    if request.method=="POST":
        text=request.POST.get('text','default')
        trans=Translator()
        
        lang=trans.detect(text)
        t_marathi=trans.translate(text,dest='mr')
    

        alt=True
        param={"ortext":text,"text":t_marathi.text,"alt":alt}
        return render(request,'EnglishToMarathi_Transl.html',param)
    return render(request,'EnglishToMarathi_Transl.html')
def EnglishToGerman(request):
    if request.method=="POST":
        text=request.POST.get('text','default')
        trans=Translator()
        
        lang=trans.detect(text)
        t=trans.translate(text,dest='de')
      

        alt=True
        param={"ortext":text,"text":t.text,"alt":alt}
        return render(request,'EnglishToGerman_Transl.html',param)
    return render(request,'EnglishToGerman_Transl.html')
def EnglishToFrench(request):
    if request.method=="POST":
        text=request.POST.get('text','default')
        trans=Translator()
        
        lang=trans.detect(text)
        t=trans.translate(text,dest='fr')
      

        alt=True
        param={"ortext":text,"text":t.text,"alt":alt}
        return render(request,'EnglishToFrench_Transl.html',param)
    return render(request,'EnglishToFrench_Transl.html')
def EnglishToArabian(request):
    if request.method=="POST":
        text=request.POST.get('text','default')
        trans=Translator()
        
        lang=trans.detect(text)
        t=trans.translate(text,dest='ar')
      

        alt=True
        param={"ortext":text,"text":t.text,"alt":alt}
        return render(request,'EnglishToArabian_Transl.html',param)
    return render(request,'EnglishToArabian_Transl.html')

#calculator
def Basic_calculator(request):
    return render(request,'basic_calculator.html')
def Loan_calculator(request):
    return render(request,'loan_calculator.html')
def GCD_calculator(request):
    return render(request,'GCD_calculator.html')
def BMI_calculator(request):
    return render(request,'BMI_calculator.html')
def TAX_calculator(request):
    return render(request,'TAX_calculator.html')
def Postfix_calculator(request):
    return render(request,'Postfix_calculator.html')
#contact
def ContactMe(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        than=True
        return render(request,'Contact_me.html',{"than":than})
    return render(request,'Contact_me.html')
def Aboutme(request):
    return render(request,'Aboutme.html')
