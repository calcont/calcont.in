from .. import MyFunctions

tran = MyFunctions.TranslatorFun()

def EnglishToHindi(request):
    respons = tran.EnglishToOther(
        request, 0, 'hi', '../templates/Translator/EnglishToOther/EnglishToHindi_Transl.html')
    return respons


def EnglishToMarathi(request):
    respons = tran.EnglishToOther(
        request, 1, 'mr', '../templates/Translator/EnglishToOther/EnglishToMarathi_Transl.html')
    return respons


def EnglishToGerman(request):
    respons = tran.EnglishToOther(
        request, 2, 'de', '../templates/Translator/EnglishToOther/EnglishToGerman_Transl.html')
    return respons


def EnglishToFrench(request):
    respons = tran.EnglishToOther(
        request, 3, 'fr', '../templates/Translator/EnglishToOther/EnglishToFrench_Transl.html')
    return respons


def EnglishToArabian(request):
    respons = tran.EnglishToOther(
        request, 4, 'ar', '../templates/Translator/EnglishToOther/EnglishToArabian_Transl.html')
    return respons


def EnglishToSpanish(request):
    respons = tran.EnglishToOther(
        request, 5, 'es', '../templates/Translator/EnglishToOther/EnglishToSpanish_Transl.html')
    return respons


def EnglishTothai(request):
    respons = tran.EnglishToOther(
        request, 6, 'th', '../templates/Translator/EnglishToOther/EnglishToThai_Transl.html')
    return respons

# hindi.to english


def HindiToEnglish(request):
    respons = tran.HindiToOther(
        request, 7, 'en', 'hi', '../templates/Translator/HindiToOther/HindiToEnglish_Transl.html')
    return respons


def HindiToMarathi(request):
    respons = tran.HindiToOther(
        request, 8, 'mr', 'hi', '../templates/Translator/HindiToOther/HindiToMarathi_Transl.html')
    return respons


def HindiToGerman(request):
    respons = tran.HindiToOther(
        request, 9, 'de', 'hi', '../templates/Translator/HindiToOther/HindiToGerman_Transl.html')
    return respons


def HindiToFrench(request):
    respons = tran.HindiToOther(
        request, 10, 'fr', 'hi', '../templates/Translator/HindiToOther/HindiToFrench_Transl.html')
    return respons


def HindiToArabian(request):
    respons = tran.HindiToOther(
        request, 11, 'ar', 'hi', '../templates/Translator/HindiToOther/HindiToArabian_Transl.html')
    return respons


def HindiToSpanish(request):
    respons = tran.HindiToOther(
        request, 12, 'es', 'hi', '../templates/Translator/HindiToOther/HindiToSpanish_Transl.html')
    return respons


def HindiToThai(request):
    respons = tran.HindiToOther(
        request, 13, 'th', 'hi', '../templates/Translator/HindiToOther/HindiToThai_Transl.html')
    return respons
