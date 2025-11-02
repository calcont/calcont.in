from .. import all_views
from django.urls import path


def urlpatterns():
    urlspatterns = [
        path('Conversion/BinaryConverter/',
             all_views.views_converters.Binaryconversion, name='Binaryconversion'),
        path('Conversion/DecimalConverter/',
             all_views.views_converters.Decimalconversion, name="Decimalconversion"),
        path('Conversion/HexadecimalConverter/',
             all_views.views_converters.Hexadecimalconversion, name="Hexadecimalconversion"),
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
        # epoch timestamp converter
        path('Conversion/Epoch_Timestamp_Converter/',
             all_views.views_converters.Epoch_Timestamp_Converter, name="Epoch_Timestamp_Converter"),
        # IST to UTC converter
        path('Conversion/IST_UTC_Converter/',
             all_views.views_converters.IST_UTC_Converter, name="IST_UTC_Converter"),
    ]
    return urlspatterns
