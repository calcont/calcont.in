from django.contrib import admin
from django.urls import path,include
from . import views
app_name="mysite"
urlpatterns = [
     
     
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
    path('Conversion/UnitsConverter/', views.Unitconversion,name="Unitconversion"),
    #meter
    path('Conversion/UnitsConverter/m_to_cm', views.Unit_mtocm_conversion,name="Unit_mtocm_conversion"),
    path('Conversion/UnitsConverter/m_to_mm', views.Unit_mtomm_conversion,name="Unit_mtomm_conversion"),
    path('Conversion/UnitsConverter/m_to_inch', views.Unit_mtoinch_conversion,name="Unit_mtoinch_conversion"),
    path('Conversion/UnitsConverter/m_to_foot', views.Unit_mtofoot_conversion,name="Unit_mtofoot_conversion"),
    path('Conversion/UnitsConverter/m_to_mile', views.Unit_mtomile_conversion,name="Unit_mtomile_conversion"),
    path('Conversion/UnitsConverter/m_to_yard', views.Unit_mtoyard_conversion,name="Unit_mtoyard_conversion"),
    path('Conversion/UnitsConverter/m_to_angstrom', views.Unit_mtoangstrom_conversion,name="Unit_mtoangstrom_conversion"),
    #cm
    path('Conversion/UnitsConverter/cm_to_mm', views.Unit_cmtomm_conversion,name="Unit_cmtomm_conversion"),
    path('Conversion/UnitsConverter/cm_to_inch', views.Unit_cmtoinch_conversion,name="Unit_cmtoinch_conversion"),
    path('Conversion/UnitsConverter/cm_to_foot', views.Unit_cmtofoot_conversion,name="Unit_cmtofoot_conversion"),
    path('Conversion/UnitsConverter/cm_to_mile', views.Unit_cmtomile_conversion,name="Unit_cmtomile_conversion"),
    path('Conversion/UnitsConverter/cm_to_yard', views.Unit_cmtoyard_conversion,name="Unit_cmtoyard_conversion"),
    path('Conversion/UnitsConverter/cm_to_angstrom', views.Unit_cmtoangstrom_conversion,name="Unit_cmtoangstrom_conversion"),
    #infix to postfix
    path('Conversion/infix_to_postfix', views.infix_to_postfix),
    #Cgpa to percentage
    path('Conversion/cgpa_to_percentage/', views.cgpa_to_percentage),
 
   

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
#PrivacyPolicy
    path('Privacy_policy/', views.PrivacyPolicy,name="PrivacyPolicy"),

    



    
]