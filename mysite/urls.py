from django.contrib import admin
from django.urls import path,include
from . import views
app_name="mysite"
handler404 = 'mysite.views.error_404'
handler500 = 'mysite.views.error_500'
urlpatterns = [
     
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', views.index,name='index'),
    path('Contact_me/', views.ContactMe,name='contact'),
    path('About/',views.Aboutme,name="about"),
    path('Supportme/',views.Supportme,name="support"),
    path('Sitemaps/',views.sitemaps),
#Authentication
    path('login/',views.Login,name="Login"),
    path('signin/',views.Signin,name="Signin"),
    path('logout/',views.Logout,name="Logout"),
    

    #Analyzer
    path('Analyzer/TextAnalyzer/', views.text,name='text'),
    # path('Analyzer/TextAnalyzer/Analyze/', views.analyze,name='analyze'),
    path('Analyzer/name_sorting/', views.name_sorting,name="name_sorting"),
    path('Analyzer/Grammar_correction/',views.Grammar_correction,name="grammar"),    
    path('Analyzer/Online-Keywords-extractor-from-text/',views.KeywordsExtraction,name="KeywordsExtraction"),
    path('Analyzer/text-to-base64-converter/',views.texttobase64,name="texttobase64"),
    path('Analyzer/base64-to-text-converter/',views.base64totext,name="base64totext"),
    path('Analyzer/text-to-image-converter/',views.texttoimage,name="texttoimage"),
    path('Analyzer/image-to-text-converter/',views.imagetotext,name="imagetotext"),
    path('Analyzer/Language-Identifier/',views.LangIdenti,name="LangIdenti"),
    path('Analyzer/Caesar-cipher-encoder-decoder/',views.caesarCipher,name="caesarCipher"),
    path('Analyzer/playfair-cipher-encoder-decoder/',views.playfCipher,name="playfCipher"),
    
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
    #image to base64 converter
    path('Conversion/Image_to_base64_Converter/', views.Image_to_base64,name="Image_to_base64"),
 #base4 to Image converter
    path('Conversion/Base64_to_Image_Converter/', views.Base64_to_Image,name="Base64_to_Image"),
   

#NameSorting
#Translator
    path('Translator/English_to_hindi/', views.EnglishToHindi,name="EnglishToHindi"),
    path('Translator/English_to_Marathi/', views.EnglishToMarathi,name="EnglishToMarathi"),
    path('Translator/English_to_German/', views.EnglishToGerman,name="EnglishToGerman"),
    path('Translator/English_to_French/', views.EnglishToFrench,name="EnglishToFrench"),
    path('Translator/English_to_Arabian/', views.EnglishToArabian,name="EnglishToArabian"),
    path('Translator/English_to_spanish/', views.EnglishToSpanish,name="EnglishToSpanish"),
    path('Translator/English_to_thai/', views.EnglishTothai,name="EnglishToThai"),
    #hindi to ..
    path('Translator/Hindi_to_English/', views.HindiToEnglish,name="HindiToEnglish"),
    path('Translator/Hindi_to_Marathi/', views.HindiToMarathi,name="HindiToMarathi"),
    path('Translator/Hindi_to_German/', views.HindiToGerman,name="HindiToGerman"),
    path('Translator/Hindi_to_French/', views.HindiToFrench,name="HindiToFrench"),
    path('Translator/Hindi_to_Arabian/', views.HindiToArabian,name="HindiToArabian"),
    path('Translator/Hindi_to_Spanish/', views.HindiToSpanish,name="HindiToSpanish"),
    path('Translator/Hindi_to_Thai/', views.HindiToThai,name="HindiToThai"),
  
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
    #Material weight calculator
    path('Calculator/Material-weight-calculator/', views.material_weight_calculator,name="material_weight_calculator"),
    #Linear regression calculator
    path('/Calculator/Linear-regression-calculator/', views.Linear_regression_calculator,name="Linear_regression_calculator"),
#PrivacyPolicy
    path('Privacy_policy/', views.PrivacyPolicy,name="PrivacyPolicy"),

    



    
]