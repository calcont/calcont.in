from .. import all_views
from django.contrib import admin
from django.urls import path, include


app_name = "mysite"
handler404 = 'mysite.all_views.views_errors.error_404'
handler500 = 'mysite.all_views.views_errors.error_500'

def urlpatterns():
    urlpatterns = [
        path('', all_views.other_views.index, name='index'),
        path('Contact_me/', all_views.other_views.ContactMe, name='contact'),
        path('About/', all_views.other_views.Aboutme, name="about"),
        path('Supportme/', all_views.other_views.Supportme, name="support"),
        path('Sitemaps/', all_views.other_views.sitemaps),
        # PrivacyPolicy
        path('Privacy_policy/', all_views.other_views.PrivacyPolicy,
             name="PrivacyPolicy"),
    ]
    return urlpatterns
