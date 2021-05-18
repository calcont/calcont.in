from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.index,name='index'),
    path('Contact_me/', views.ContactMe,name='text'),
    path('About/',views.Aboutme),

#Authentication
    path('login/',views.Login),
    path('signin/',views.Signin),
    path('logout/',views.Logout),
    # path('', views.index,name='')),
    # path('conversion', views.convesion,name='conversion'),
    #Analyzer
    path('Analyzer/TextAnalyzer/', views.text,name='text'),
    # path('Analyzer/TextAnalyzer/Analyze/', views.analyze,name='analyze'),
    path('Analyzer/name_sorting/', views.name_sorting),
    path('Analyzer/Grammar_correction/',views.Grammar_correction),    
    path('Conversion/BinaryConverter/', views.Binaryconversion,name='BintoDec'),
    path('Conversion/DecimalConverter/', views.Decimalconversion),
    path('Conversion/HexadecimalConverter/', views.Hexadecimalconversion),
#Conversion
    #CurrencyConverter
    path('Conversion/CurrencyConverter/', views.Currencyconversion),
    path('Conversion/UnitsConverter/', views.Unitconversion),
    #meter
    path('Conversion/UnitsConverter/m_to_cm', views.Unit_mtocm_conversion),
    path('Conversion/UnitsConverter/m_to_mm', views.Unit_mtomm_conversion),
    path('Conversion/UnitsConverter/m_to_inch', views.Unit_mtoinch_conversion),
    path('Conversion/UnitsConverter/m_to_foot', views.Unit_mtofoot_conversion),
    path('Conversion/UnitsConverter/m_to_mile', views.Unit_mtomile_conversion),
    path('Conversion/UnitsConverter/m_to_yard', views.Unit_mtoyard_conversion),
    path('Conversion/UnitsConverter/m_to_angstrom', views.Unit_mtoangstrom_conversion),
    #cm
    path('Conversion/UnitsConverter/cm_to_mm', views.Unit_cmtomm_conversion),
    path('Conversion/UnitsConverter/cm_to_inch', views.Unit_cmtoinch_conversion),
    path('Conversion/UnitsConverter/cm_to_foot', views.Unit_cmtofoot_conversion),
    path('Conversion/UnitsConverter/cm_to_mile', views.Unit_cmtomile_conversion),
    path('Conversion/UnitsConverter/cm_to_yard', views.Unit_cmtoyard_conversion),
    path('Conversion/UnitsConverter/cm_to_angstrom', views.Unit_cmtoangstrom_conversion),
    #infix to postfix
    path('Conversion/infix_to_postfix', views.infix_to_postfix),
 

   

#NameSorting
#Translator
    path('Translator/English_to_hindi/', views.EnglishToHindi),
    # path('voice_recognition/', views.voice_recognition),

    path('Translator/English_to_Marathi/', views.EnglishToMarathi),
    path('Translator/English_to_German/', views.EnglishToGerman),
    path('Translator/English_to_French/', views.EnglishToFrench),
    path('Translator/English_to_Arabian/', views.EnglishToArabian),
    # path('Translator/English_to_hindi', views.EnglishToHindi),
    # path('Translator/English_to_hindi', views.EnglishToHindi),
    # path('Translator/English_to_hindi', views.EnglishToHindi),
    # path('Translator/English_to_hindi', views.EnglishToHindi),
#calculator
  
    #Loancalculator
    path('Calculator/EMI_calculator/', views.Loan_calculator),
    #gcd calculator
    path('Calculator/GCD_calculator/', views.GCD_calculator),
    #BMI calculator
    path('Calculator/BMI_calculator/', views.BMI_calculator),
    #tax calculator

    path('Calculator/Postfix_calculator/', views.Postfix_calculator),
    #PrivacyPolicy
    path('Privacy_policy/', views.PrivacyPolicy),



    
]