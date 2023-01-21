from .. import all_views
from django.urls import path


def urlpatterns():
    urlpatterns = [
        # Translator
        path('Translator/English_to_hindi/',
             all_views.views_translators.EnglishToHindi, name="EnglishToHindi"),
        path('Translator/English_to_Marathi/',
             all_views.views_translators.EnglishToMarathi, name="EnglishToMarathi"),
        path('Translator/English_to_German/',
             all_views.views_translators.EnglishToGerman, name="EnglishToGerman"),
        path('Translator/English_to_French/',
             all_views.views_translators.EnglishToFrench, name="EnglishToFrench"),
        path('Translator/English_to_Arabian/',
             all_views.views_translators.EnglishToArabian, name="EnglishToArabian"),
        path('Translator/English_to_spanish/',
             all_views.views_translators.EnglishToSpanish, name="EnglishToSpanish"),
        path('Translator/English_to_thai/',
             all_views.views_translators.EnglishTothai, name="EnglishToThai"),
        # hindi to ..
        path('Translator/Hindi_to_English/',
             all_views.views_translators.HindiToEnglish, name="HindiToEnglish"),
        path('Translator/Hindi_to_Marathi/',
             all_views.views_translators.HindiToMarathi, name="HindiToMarathi"),
        path('Translator/Hindi_to_German/',
             all_views.views_translators.HindiToGerman, name="HindiToGerman"),
        path('Translator/Hindi_to_French/',
             all_views.views_translators.HindiToFrench, name="HindiToFrench"),
        path('Translator/Hindi_to_Arabian/',
             all_views.views_translators.HindiToArabian, name="HindiToArabian"),
        path('Translator/Hindi_to_Spanish/',
             all_views.views_translators.HindiToSpanish, name="HindiToSpanish"),
        path('Translator/Hindi_to_Thai/',
             all_views.views_translators.HindiToThai, name="HindiToThai"),
    ]
    return urlpatterns
