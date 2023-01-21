from .. import MyFunctions
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import base64
import pytesseract
import requests
import os
from django.views.decorators.csrf import csrf_exempt

SideMap = MyFunctions.ArrangeSideMapForWebpage()

# Conversion
def Binaryconversion(request):
    link_string1, link_string2 = SideMap.arrange(0, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/Binarycon.html', param)


def Decimalconversion(request):
    link_string1, link_string2 = SideMap.arrange(1, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/DecimalCon.html', param)


def Hexadecimalconversion(request):
    link_string1, link_string2 = SideMap.arrange(2, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/HexaCon.html', param)
# currency


def Currencyconversion(request):
    link_string1, link_string2 = SideMap.arrange(3, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/CurrencyCon.html', param)


def infix_to_postfix(request):
    link_string1, link_string2 = SideMap.arrange(4, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/infix_to_postfix.html', param)
# cgpatopercent


def cgpa_to_percentage(request):
    link_string1, link_string2 = SideMap.arrange(9, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/cgtopercent.html', param)
# PostfixtoInfix


def postfix_to_infix(request):
    link_string1, link_string2 = SideMap.arrange(6, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/postfix_to_infix.html', param)
# Infixtoprefix


def infix_to_prefix(request):
    link_string1, link_string2 = SideMap.arrange(5, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/infix_to_prefix.html', param)
# prefixtoPostfix


def prefix_to_postfix(request):
    link_string1, link_string2 = SideMap.arrange(7, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/prefix_to_postfix.html', param)
# prefixtoInfix

def prefix_to_infix(request):
    link_string1, link_string2 = SideMap.arrange(8, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/prefix_to_infix.html', param)

# Image to base64 converter


@csrf_exempt
def Image_to_base64(request):
    link_string1, link_string2 = SideMap.arrange(10, 2, 'CC')
    if request.method == "POST":
        try:
            image = request.FILES['image']
            encoded_string = base64.b64encode(image.read())
        except:
            url = request.POST.get('url')
            response = requests.get(url)
            encoded_string = base64.b64encode(response.content)
        response = json.dumps({'txt': encoded_string.decode()}, default=str)
        return HttpResponse(response)

    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/image_to_base64.html', param)

# Base64 to Image Converter


def Base64_to_Image(request):
    link_string1, link_string2 = SideMap.arrange(11, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/Base64_to_Image.html', param)
