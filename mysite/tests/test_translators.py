import html
import json

from django.test import TestCase
from django.urls import reverse

ENGLISH_TO_OTHER_TEMPLATE = '../templates/Translator/EnglishToOther/'
HINDI_TO_OTHER_TEMPLATE = '../templates/Translator/HindiToOther/'


class BaseTranslatorTestCase(TestCase):
    def setUp(self):
        self.dummy_request = {
            'text': 'My name is Amar'
        }


class EnglishToOtherTestCase(TestCase):
    dummy_request = {
        'text': 'My name is Amar'
    }

    def english_to_other(self, controller_name, expected_text):
        response = self.client.post(reverse(controller_name), data=self.dummy_request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, ENGLISH_TO_OTHER_TEMPLATE + controller_name + '_Transl.html')
        decoded_html = html.unescape(response.content.decode('utf-8'))
        self.assertContains(response, expected_text)
        
    def test_english_to_hindi(self):
        self.english_to_other('EnglishToHindi', 'मेरा नाम अमर है')

    def test_english_to_marathi(self):
        self.english_to_other('EnglishToMarathi', 'माझं नाव अमर आहे')

    def test_english_to_german(self):
        self.english_to_other('EnglishToGerman', 'Mein Name ist Amar')

    def test_english_to_french(self):
        self.english_to_other('EnglishToFrench', "Je m’appelle Amar")
    #
    def test_english_to_arabian(self):
        self.english_to_other('EnglishToArabian', 'اسمي عمار')

    def test_english_to_spanish(self):
        self.english_to_other('EnglishToSpanish', 'Mi nombre es Amar')

    def test_english_to_thai(self):
        self.english_to_other('EnglishToThai', 'ฉันชื่ออามาร์')


class HindiToOtherTestCase(TestCase):
    dummy_request = {
        'text': 'मेरा नाम अमर है'
    }

    def hindi_to_other(self, controller_name, expected_text):
        response = self.client.post(reverse(controller_name), data=self.dummy_request)
        self.assertEqual(response.status_code, 200)
        decoded_json = json.loads(response.content)
        self.assertEqual(decoded_json['ConTex'], expected_text)

    def test_hindi_to_english(self):
        self.hindi_to_other('HindiToEnglish', 'My name is Amar')

    def test_hindi_to_marathi(self):
        self.hindi_to_other('HindiToMarathi', 'माझं नाव अमर आहे.')

    def test_hindi_to_german(self):
        self.hindi_to_other('HindiToGerman', 'Mein Name ist Amar')

    def test_hindi_to_french(self):
        self.hindi_to_other('HindiToFrench', "Je m’appelle Amar")

    def test_hindi_to_spanish(self):
        self.hindi_to_other('HindiToSpanish', 'Mi nombre es Amar')

    def test_hindi_to_thai(self):
        self.hindi_to_other('HindiToThai', 'ฉันชื่ออามาร์')
