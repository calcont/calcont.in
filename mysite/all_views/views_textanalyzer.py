from .. import MyFunctions
from django.shortcuts import render
from django.http import HttpResponse
import json
from rake_nltk import Rake
import base64
import os
from PIL import Image
from googletrans import Translator
import googletrans
import pytesseract
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt

SideMap = MyFunctions.ArrangeSideMapForWebpage()
if os.getcwd() != '/app':  # for windows
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'  # do install tesseact in this path only and add it to your environment-variables
else:
    pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'


def text(request):
    link_string1, link_string2 = SideMap.arrange(0, 1, 'AT')
    if request.method == "POST":
        tex = request.POST.get('text', 'default')
        removepunc = request.POST.get('removepunc', 'off')
        fullcaps = request.POST.get('fullcaps', 'off')
        newlineremover = request.POST.get('newlineremover', 'off')
        xtraspaceremover = request.POST.get('xtraspaceremover', 'off')
        # print(tex)
        IsEnter = True
        if removepunc == 'on':
            pun = '''!.()-[]{};:'"/\,<>?@#$%^_~'''
            analysed = ""
            for char in tex:
                if char not in pun:
                    analysed = analysed + char
        if fullcaps == 'on':
            analysed = tex.upper()
        if newlineremover == "on":
            analysed = ""
            for char in tex:
                if char != '\n' and char != '\r':
                    analysed += char
        if xtraspaceremover == "on":
            analysed = ""
            for i, char in enumerate(tex):
                if not (tex[i] == " "):
                    analysed += char

        if fullcaps != 'on' and removepunc != "on" and xtraspaceremover != "on" and newlineremover != "on":

            analysed = "PLEASE SELECT OPERATION."
        if tex == "":
            analysed = "PLEASE ENTER TEXT FIRST."

        parms = {'Text': analysed, 'IsEnter': IsEnter, 'OrText': tex,
                 'link_string1': link_string1, 'link_string2': link_string2}
        return render(request, '../templates/textAnalyzer/text.html', parms)
    params = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/textAnalyzer/text.html', params)


def Grammar_correction(request):
    link_string1, link_string2 = SideMap.arrange(2, 1, 'AT')
    if request.method == 'POST':
        IsEnter = True
        text = request.POST.get('text', 'default')
        from .. import ginger
        length_text = len(text)
        if length_text < 300:
            result = ginger.gingerI().parse(text)
            n = len(list(result['corrections']))
            d = []
            a = []
            for i in range(n):
                dash = list(result['corrections'][i].items())
                d.append(dash[0][1])
            d.reverse()
            i = 0
            while i < (len(text)):
                if i in d:
                    for j in range(i, len(text)):
                        if text[j] == " ":
                            break
                    a.append("\u0332".join(text[i:j + 1]))
                    i = j
                else:
                    a.append(text[i])
                i += 1
            Text = "".join(a)

            param = {'NewText': result['result'], "text": Text, "IsEnter": IsEnter,
                     "length_text": length_text, 'link_string1': link_string1, 'link_string2': link_string2}
        else:
            param = {'NewText': " ", "text": text, "IsEnter": IsEnter, "length_text": length_text,
                     'link_string1': link_string1, 'link_string2': link_string2}
        return render(request, '../templates/textAnalyzer/Grammar_correction.html', param)
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/textAnalyzer/Grammar_correction.html', param)

# namesorting


def name_sorting(request):
    link_string1, link_string2 = SideMap.arrange(1, 1, 'AT')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/textAnalyzer/name_sorting.html', param)

# KeywordsExtractionFromText


def KeywordsExtraction(request):
    link_string1, link_string2 = SideMap.arrange(3, 1, 'AT')
    try:
        if request.method == "POST":
            text = request.POST['text']
            rake_nltk_var = Rake()
            rake_nltk_var.extract_keywords_from_text(text)
            keyword_extracted = rake_nltk_var.get_ranked_phrases()
            response = json.dumps({'Keyword': keyword_extracted, 'keywordLen': len(
                keyword_extracted)}, default=str)
            return HttpResponse(response)
    except Exception as e:
        print(e)
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/textAnalyzer/KeywwordsExtraction.html', param)


def texttobase64(request):
    link_string1, link_string2 = SideMap.arrange(4, 1, 'AT')
    if request.method == "POST":
        text = request.POST['text']
        encoded_string = base64.b64encode(text.encode())
        encoded_string = encoded_string.decode()
        response = json.dumps({'Encoded': encoded_string}, default=str)
        return HttpResponse(response)
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/textAnalyzer/text_to_base64.html', param)

# base64 to text


def base64totext(request):
    link_string1, link_string2 = SideMap.arrange(5, 1, 'AT')
    if request.method == "POST":
        try:
            text = request.POST['text']
            decoded_string = base64.b64decode(text.encode())
            decoded_string = decoded_string.decode()
            response = json.dumps({'Decoded': decoded_string}, default=str)
        except Exception:
            response = json.dumps({'Decoded': "There is some Error while processing"}, default=str)
        return HttpResponse(response)
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/textAnalyzer/base64_to_text.html', param)

# texttoimage


def texttoimage(request):
    link_string1, link_string2 = SideMap.arrange(6, 1, 'AT')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/textAnalyzer/texttoimage.html', param)


@csrf_exempt
def imagetotext(request):
    link_string1, link_string2 = SideMap.arrange(7, 1, 'AT')
    if request.method == "POST":
        try:
            image = request.FILES['image']
            img = Image.open(image)
            result = pytesseract.image_to_string(img)
        except Exception as e:
            print(e)
            url = request.POST.get('url')
            import requests
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            result = pytesseract.image_to_string(img)

        response = json.dumps({'txt': result}, default=str)
        return HttpResponse(response)
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/textAnalyzer/Imagetotext.html', param)

# Language identifier


def LangIdenti(request):
    link_string1, link_string2 = SideMap.arrange(8, 1, 'AT')
    t = Translator()
    if request.method == "POST":
        text = request.POST['text']
        if request.POST.get('isDetect') == "0":
            eng_txt = t.translate(text, dest='en')
            response = json.dumps({'e_lang': eng_txt.text}, default=str)
        else:
            try:
                lang = t.detect(text)
                response = json.dumps(
                    {'lang': googletrans.LANGUAGES[lang.lang]}, default=str)
            except Exception:
                err = "Not able to detect this text.This might me due to some special characters or some other reason.Can you please try some other text?"
                response = json.dumps({'lang': err}, default=str)
        return HttpResponse(response)
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/textAnalyzer/LangIdenti.html', param)
# Caesar cipher encoder/decoder


def caesarCipher(request):
    link_string1, link_string2 = SideMap.arrange(9, 1, 'AT')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/textAnalyzer/CaesarCipher.html', param)

# playfair cipher encoder/decoder


def playfCipher(request):
    link_string1, link_string2 = SideMap.arrange(10, 1, 'AT')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/textAnalyzer/playfCipher.html', param)
