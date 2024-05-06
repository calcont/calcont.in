import langdetect
from pycountry import languages
from deep_translator import GoogleTranslator
import logging


def detect_language(text):
    detected_lang_code = langdetect.detect(text)
    detected_lang = languages.get(alpha_2=detected_lang_code).name
    return detected_lang


def translate_text(text, src='auto', target='en'):
    try:
        translated_text = GoogleTranslator(source=src, target=target).translate(text)
    except Exception as e:
        logging.error(e)
        translated_text = "Sorry, translation failed. Please try again later."
    return translated_text
