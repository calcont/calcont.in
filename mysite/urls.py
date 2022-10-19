from django.contrib import admin
from django.urls import path, include
from . import all_views

app_name = "mysite"
handler404 = 'mysite.all_views.views_errors.error_404'
handler500 = 'mysite.all_views.views_errors.error_500'
urlpatterns = [

    path('oauth/', include('social_django.urls', namespace='social')),
    path('', all_views.other_views.index, name='index'),
    path('Contact_me/', all_views.other_views.ContactMe, name='contact'),
    path('About/', all_views.other_views.Aboutme, name="about"),
    path('Supportme/', all_views.other_views.Supportme, name="support"),
    path('Sitemaps/', all_views.other_views.sitemaps),
    # Authentication
    path('login/', all_views.views_authentication.Login, name="Login"),
    path('signin/', all_views.views_authentication.Signin, name="Signin"),
    path('logout/', all_views.views_authentication.Logout, name="Logout"),


    # Analyzer
    path('Analyzer/TextAnalyzer/', all_views.views_textanalyzer.text, name='text'),
    # path('Analyzer/TextAnalyzer/Analyze/', views.analyze,name='analyze'),
    path('Analyzer/name_sorting/',
         all_views.views_textanalyzer.name_sorting, name="name_sorting"),
    path('Analyzer/Grammar_correction/',
         all_views.views_textanalyzer.Grammar_correction, name="grammar"),
    path('Analyzer/Online-Keywords-extractor-from-text/',
         all_views.views_textanalyzer.KeywordsExtraction, name="KeywordsExtraction"),
    path('Analyzer/text-to-base64-converter/',
         all_views.views_textanalyzer.texttobase64, name="texttobase64"),
    path('Analyzer/base64-to-text-converter/',
         all_views.views_textanalyzer.base64totext, name="base64totext"),
    path('Analyzer/text-to-image-converter/',
         all_views.views_textanalyzer.texttoimage, name="texttoimage"),
    path('Analyzer/image-to-text-converter/',
         all_views.views_textanalyzer.imagetotext, name="imagetotext"),
    path('Analyzer/Language-Identifier/',
         all_views.views_textanalyzer.LangIdenti, name="LangIdenti"),
    path('Analyzer/Caesar-cipher-encoder-decoder/',
         all_views.views_textanalyzer.caesarCipher, name="caesarCipher"),
    path('Analyzer/playfair-cipher-encoder-decoder/',
         all_views.views_textanalyzer.playfCipher, name="playfCipher"),

    path('Conversion/BinaryConverter/',
         all_views.views_converters.Binaryconversion, name='Binaryconversion'),
    path('Conversion/DecimalConverter/',
         all_views.views_converters.Decimalconversion, name="Decimalconversion"),
    path('Conversion/HexadecimalConverter/',
         all_views.views_converters.Hexadecimalconversion, name="Hexadecimalconversion"),
    # Conversion
    # CurrencyConverter
    path('Conversion/CurrencyConverter/',
         all_views.views_converters.Currencyconversion, name="Currencyconversion"),
    path('Conversion/infix_to_postfix',
         all_views.views_converters.infix_to_postfix, name="infix_to_postfix"),
    # infix to prefix
    path('Conversion/infix_to_prefix',
         all_views.views_converters.infix_to_prefix, name="infix_to_prefix"),
    # postfix to infix
    path('Conversion/postfix_to_infix',
         all_views.views_converters.postfix_to_infix, name="postfix_to_infix"),
    # prefix to infix
    path('Conversion/prefix_to_infix',
         all_views.views_converters.prefix_to_infix, name="prefix_to_infix"),
    # prefix to postfix
    path('Conversion/prefix_to_postfix',
         all_views.views_converters.prefix_to_postfix, name="prefix_to_postfix"),
    # Cgpa to percentage
    path('Conversion/cgpa_to_percentage/',
         all_views.views_converters.cgpa_to_percentage, name="cgpa_to_percentage"),
    # image to base64 converter
    path('Conversion/Image_to_base64_Converter/',
         all_views.views_converters.Image_to_base64, name="Image_to_base64"),
    # base4 to Image converter
    path('Conversion/Base64_to_Image_Converter/',
         all_views.views_converters.Base64_to_Image, name="Base64_to_Image"),


    # NameSorting
    # Translator
    path('Translator/English_to_hindi/',
         all_views.views_translators.EnglishToHindi, name="EnglishToHindi"),
    path('Translator/English_to_Marathi/',
         all_views.views_translators.EnglishToMarathi, name="EnglishToMarathi"),
    path('Translator/English_to_German/',
         all_views.views_translators.EnglishToGerman, name="EnglishToGerman"),
    path('Translator/English_to_French/',
         all_views.views_translators.EnglishToFrench, name="EnglishToFrench"),
    path('Translator/English_to_Arabian/',
         all_views.views_translators.EnglishToArabian, name="EnglishToArabian"),
    path('Translator/English_to_spanish/',
         all_views.views_translators.EnglishToSpanish, name="EnglishToSpanish"),
    path('Translator/English_to_thai/',
         all_views.views_translators.EnglishTothai, name="EnglishToThai"),
    # hindi to ..
    path('Translator/Hindi_to_English/',
         all_views.views_translators.HindiToEnglish, name="HindiToEnglish"),
    path('Translator/Hindi_to_Marathi/',
         all_views.views_translators.HindiToMarathi, name="HindiToMarathi"),
    path('Translator/Hindi_to_German/',
         all_views.views_translators.HindiToGerman, name="HindiToGerman"),
    path('Translator/Hindi_to_French/',
         all_views.views_translators.HindiToFrench, name="HindiToFrench"),
    path('Translator/Hindi_to_Arabian/',
         all_views.views_translators.HindiToArabian, name="HindiToArabian"),
    path('Translator/Hindi_to_Spanish/',
         all_views.views_translators.HindiToSpanish, name="HindiToSpanish"),
    path('Translator/Hindi_to_Thai/',
         all_views.views_translators.HindiToThai, name="HindiToThai"),

    # calculator

    # Loancalculator
    path('Calculator/EMI_calculator/',
         all_views.views_calculators.Loan_calculator, name="Loan_calculator"),
    # gcd calculator
    path('Calculator/GCD_calculator/',
         all_views.views_calculators.GCD_calculator, name="GCD_calculator"),
    # BMI calculator
    path('Calculator/BMI_calculator/',
         all_views.views_calculators.BMI_calculator, name="BMI_calculator"),
    # postfix calculator
    path('Calculator/Postfix_calculator/',
         all_views.views_calculators.Postfix_calculator, name="Postfix_calculator"),
    # Prefix calculator
    path('Calculator/Prefix_calculator/',
         all_views.views_calculators.Prefix_calculator, name="Prefix_calculator"),
    # Material weight calculator
    path('Calculator/Material-weight-calculator/',
         all_views.views_calculators.material_weight_calculator, name="material_weight_calculator"),
    # Linear regression calculator
    path('Calculator/Linear-regression-calculator/',
         all_views.views_calculators.Linear_regression_calculator, name="Linear_regression_calculator"),
    # hcf and lcm calculator
    path('Calculator/HCF-LCM-calculator/',
         all_views.views_calculators.HCF_LCM_calculator, name="HCF_LCM_calculator"),
    # PrivacyPolicy
    path('Privacy_policy/', all_views.other_views.PrivacyPolicy, name="PrivacyPolicy"),






]
