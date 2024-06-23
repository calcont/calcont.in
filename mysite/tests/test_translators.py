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
        'text': 'my name is Amar'
    }

    def english_to_other(self, controller_name, expected_text):
        response = self.client.post(reverse(controller_name), data=self.dummy_request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, ENGLISH_TO_OTHER_TEMPLATE + controller_name + '_Transl.html')
        decoded_html = html.unescape(response.content.decode('utf-8'))
        self.assertIn(expected_text, decoded_html)

    def test_english_to_hindi(self):
        self.english_to_other('EnglishToHindi', 'मेरा नाम अमर है')

    def test_english_to_marathi(self):
        self.english_to_other('EnglishToMarathi', 'माझे नाव अमर आहे')

    def test_english_to_german(self):
        self.english_to_other('EnglishToGerman', 'mein Name ist Amar')

    def test_english_to_french(self):
        self.english_to_other('EnglishToFrench', "je m'appelle Amar")

    #
    def test_english_to_arabian(self):
        self.english_to_other('EnglishToArabian', 'اسمي عمار')

    def test_english_to_spanish(self):
        self.english_to_other('EnglishToSpanish', 'mi nombre es amar')

    def test_english_to_thai(self):
        self.english_to_other('EnglishToThai', 'ฉันชื่ออามาร์')


class HindiToOtherTestCase(TestCase):
    dummy_request = {
        'text': 'यह एक परीक्षण संदेश है'
    }

    def hindi_to_other(self, controller_name, expected_text):
        response = self.client.post(reverse(controller_name), data=self.dummy_request)
        self.assertEqual(response.status_code, 200)
        decoded_json = json.loads(response.content)
        self.assertEqual(expected_text, decoded_json['ConTex'])

    def test_hindi_to_english(self):
        self.hindi_to_other('HindiToEnglish', 'This is a test message')

    def test_hindi_to_marathi(self):
        self.hindi_to_other('HindiToMarathi', 'हा एक चाचणी संदेश आहे')

    def test_hindi_to_german(self):
        self.hindi_to_other('HindiToGerman', 'Dies ist eine Testnachricht')

    def test_hindi_to_french(self):
        self.hindi_to_other('HindiToFrench', "Ceci est un message test")

    def test_hindi_to_spanish(self):
        self.hindi_to_other('HindiToSpanish', 'Este es un mensaje de prueba')

    def test_hindi_to_thai(self):
        self.hindi_to_other('HindiToThai', 'นี่คือข้อความทดสอบ')
