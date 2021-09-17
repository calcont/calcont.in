from django.contrib import admin
from django.urls import path,include
from . import views
app_name="mysite"
urlpatterns = [
     
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', views.index,name='index'),
    path('Contact_me/', views.ContactMe,name='contact'),
    path('About/',views.Aboutme,name="about"),
#Authentication
    path('login/',views.Login,name="Login"),
    path('signin/',views.Signin,name="Signin"),
    path('logout/',views.Logout,name="Logout"),

    #Analyzer
    path('Analyzer/TextAnalyzer/', views.text,name='text'),
    # path('Analyzer/TextAnalyzer/Analyze/', views.analyze,name='analyze'),
    path('Analyzer/name_sorting/', views.name_sorting,name="name_sorting"),
    path('Analyzer/Grammar_correction/',views.Grammar_correction,name="grammar"),    
    path('Conversion/BinaryConverter/', views.Binaryconversion,name='Binaryconversion'),
    path('Conversion/DecimalConverter/', views.Decimalconversion,name="Decimalconversion"),
    path('Conversion/HexadecimalConverter/', views.Hexadecimalconversion,name="Hexadecimalconversion"),
#Conversion
    #CurrencyConverter
    path('Conversion/CurrencyConverter/', views.Currencyconversion,name="Currencyconversion"),
    path('Conversion/infix_to_postfix', views.infix_to_postfix,name="infix_to_postfix"),
    #infix to prefix
    path('Conversion/infix_to_prefix', views.infix_to_prefix,name="infix_to_prefix"),
    #postfix to infix
    path('Conversion/postfix_to_infix', views.postfix_to_infix,name="postfix_to_infix"),
     #prefix to infix
    path('Conversion/prefix_to_infix', views.prefix_to_infix,name="prefix_to_infix"),
    #prefix to postfix
    path('Conversion/prefix_to_postfix', views.prefix_to_postfix,name="prefix_to_postfix"),
    #Cgpa to percentage
    path('Conversion/cgpa_to_percentage/', views.cgpa_to_percentage,name="cgpa_to_percentage"),
 
   

#NameSorting
#Translator
    path('Translator/English_to_hindi/', views.EnglishToHindi,name="EnglishToHindi"),
    path('Translator/English_to_Marathi/', views.EnglishToMarathi,name="EnglishToMarathi"),
    path('Translator/English_to_German/', views.EnglishToGerman,name="EnglishToGerman"),
    path('Translator/English_to_French/', views.EnglishToFrench,name="EnglishToFrench"),
    path('Translator/English_to_Arabian/', views.EnglishToArabian,name="EnglishToArabian"),
  
#calculator

    #Loancalculator
    path('Calculator/EMI_calculator/', views.Loan_calculator,name="Loan_calculator"),
    #gcd calculator
    path('Calculator/GCD_calculator/', views.GCD_calculator,name="GCD_calculator"),
    #BMI calculator
    path('Calculator/BMI_calculator/', views.BMI_calculator,name="BMI_calculator"),
    #tax calculator

    path('Calculator/Postfix_calculator/', views.Postfix_calculator,name="Postfix_calculator"),
    #Prefix calculator
    path('Calculator/Prefix_calculator/', views.Prefix_calculator,name="Prefix_calculator"),
#PrivacyPolicy
    path('Privacy_policy/', views.PrivacyPolicy,name="PrivacyPolicy"),

    



    
]