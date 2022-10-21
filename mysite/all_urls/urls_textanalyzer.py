from .. import all_views
from django.contrib import admin
from django.urls import path, include


def urlpatterns():
    urlspatterns = [
        # Analyzer
        path('Analyzer/TextAnalyzer/',
             all_views.views_textanalyzer.text, name='text'),
        # path('Analyzer/TextAnalyzer/Analyze/', views.analyze,name='analyze'),
        path('Analyzer/name_sorting/',
             all_views.views_textanalyzer.name_sorting, name="name_sorting"),
        path('Analyzer/Grammar_correction/',
             all_views.views_textanalyzer.Grammar_correction, name="grammar"),
        path('Analyzer/Online-Keywords-extractor-from-text/',
             all_views.views_textanalyzer.KeywordsExtraction, name="KeywordsExtraction"),
        path('Analyzer/text-to-base64-converter/',
             all_views.views_textanalyzer.texttobase64, name="texttobase64"),
        path('Analyzer/base64-to-text-converter/',
             all_views.views_textanalyzer.base64totext, name="base64totext"),
        path('Analyzer/text-to-image-converter/',
             all_views.views_textanalyzer.texttoimage, name="texttoimage"),
        path('Analyzer/image-to-text-converter/',
             all_views.views_textanalyzer.imagetotext, name="imagetotext"),
        path('Analyzer/Language-Identifier/',
             all_views.views_textanalyzer.LangIdenti, name="LangIdenti"),
        path('Analyzer/Caesar-cipher-encoder-decoder/',
             all_views.views_textanalyzer.caesarCipher, name="caesarCipher"),
        path('Analyzer/playfair-cipher-encoder-decoder/',
             all_views.views_textanalyzer.playfCipher, name="playfCipher"),
    ]
    return urlspatterns
