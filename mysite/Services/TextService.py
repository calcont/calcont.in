import langdetect
from pycountry import languages
import translators as ts


def detect_language(text):
    detected_lang_code = langdetect.detect(text)
    detected_lang = languages.get(alpha_2=detected_lang_code).name
    return detected_lang


def translate_text(text, src='auto', target='en'):
    try:
        translated_text = ts.translate_text(text, from_language=src, to_language=target)
    except Exception:
        translated_text = "Sorry, we could not translate the text. Please try again later."
    return translated_text
