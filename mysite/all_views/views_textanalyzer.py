from .. import MyFunctions
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from rake_nltk import Rake
import os
from PIL import Image
import pytesseract
from ..Services.TextService import detect_language, translate_text
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt

SideMap = MyFunctions.ArrangeSideMapForWebpage()
if os.getcwd() != '/app':  # for windows
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'  # do install tesseract in this path only and add it to your environment-variables
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
    if request.method == "POST":
        text = request.POST['text']
        url = os.environ.get('GRAMMAR_API_URL')
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": os.environ.get('GRAMMAR_API_KEY'),
            "X-RapidAPI-Host": os.environ.get('GRAMMAR_API_HOST')
        }
        response = requests.post(url, data=request.POST, headers=headers)
        response = response.json()
        errors = response['response']['errors']
        reversed_errors = reversed(errors)

        corrected_text = text
        for error in reversed_errors:
            correction = error['better'][0]
            corrected_text = corrected_text[:error['offset']] + correction + corrected_text[
                                                                             error['offset'] + error['length']:]
        return HttpResponse(corrected_text)
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
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/textAnalyzer/text_to_base64.html', param)


# base64 to text


def base64totext(request):
    link_string1, link_string2 = SideMap.arrange(5, 1, 'AT')
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
        except Exception:
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
    if request.method == "POST":
        text = request.POST['text']
        if request.POST.get('isDetect') == "0":
            translated_text = translate_text(text)
            response = json.dumps({'e_lang': translated_text}, default=str)
        else:
            try:
                detected_lang = detect_language(text)
                response = json.dumps({'lang': detected_lang}, default=str)
            except Exception:
                err = "Not able to detect this text.This might be due to some special characters or some other reason.Can you please try some other text?"
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
