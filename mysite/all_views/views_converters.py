from django.shortcuts import render
from django.http import HttpResponse
import json
import base64
import requests
import random
import logging
from django.core.cache import cache
from .. import MyFunctions
from ..constants import converters as constants
from ..handlers.requestHandler.get import GetHandler

SideMap = MyFunctions.ArrangeSideMapForWebpage()
CACHE_TIMEOUT = 60 * 60 * 24
logger = logging.getLogger(__name__)


def generate_currency_endpoint(from_currency):
    endpoint_key = random.choice([constants.ENDPOINT_KEY1, constants.ENDPOINT_KEY2])
    currencies_queryparam = ','.join(constants.CURRENCIES)
    endpoint = f"{constants.CURRENCY_ENDPOINT}/?apikey={endpoint_key}&base_currency={from_currency}&currencies={currencies_queryparam}"
    return endpoint


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


def Currencyconversion(request):
    link_string1, link_string2 = SideMap.arrange(3, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    if request.method == "POST":
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = request.POST.get('amount')
        if cache.get(from_currency) is None:
            endpoint = generate_currency_endpoint(from_currency)
            get_request = GetHandler(endpoint)
            response = get_request.send()
            cache.set(from_currency, response, CACHE_TIMEOUT)
            logger.info(f"Cache miss for {from_currency}. Data fetched from API.")
        data = cache.get(from_currency).json()
        logger.info(f"Cache hit for {from_currency}. Data fetched from cache.")
        conversion_rate = data['data'][to_currency]['value']
        converted_amount = float(amount) * conversion_rate
        json_response = json.dumps({'converted_amount': converted_amount}, default=str)
        return HttpResponse(json_response)
    return render(request, '../templates/converter/CurrencyCon.html', param)


def infix_to_postfix(request):
    link_string1, link_string2 = SideMap.arrange(4, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/infix_to_postfix.html', param)


def cgpa_to_percentage(request):
    link_string1, link_string2 = SideMap.arrange(9, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/cgtopercent.html', param)


def postfix_to_infix(request):
    link_string1, link_string2 = SideMap.arrange(6, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/postfix_to_infix.html', param)


def infix_to_prefix(request):
    link_string1, link_string2 = SideMap.arrange(5, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/infix_to_prefix.html', param)


def prefix_to_postfix(request):
    link_string1, link_string2 = SideMap.arrange(7, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/prefix_to_postfix.html', param)


def prefix_to_infix(request):
    link_string1, link_string2 = SideMap.arrange(8, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/prefix_to_infix.html', param)


def Image_to_base64(request):
    link_string1, link_string2 = SideMap.arrange(10, 2, 'CC')
    if request.method == "POST":
        try:
            image = request.FILES['image']
            encoded_string = base64.b64encode(image.read())
        except Exception:
            url = request.POST.get('url')
            response = requests.get(url)
            encoded_string = base64.b64encode(response.content)
        response = json.dumps({'txt': encoded_string.decode()}, default=str)
        return HttpResponse(response)

    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/image_to_base64.html', param)


def Base64_to_Image(request):
    link_string1, link_string2 = SideMap.arrange(11, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/Base64_to_Image.html', param)


def Epoch_Timestamp_Converter(request):
    link_string1, link_string2 = SideMap.arrange(12, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/epoch_timestamp_converter.html', param)


def IST_UTC_Converter(request):
    link_string1, link_string2 = SideMap.arrange(13, 2, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/converter/ist_utc_converter.html', param)