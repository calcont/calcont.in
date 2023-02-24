from .. import all_views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from ..sitemaps import StaticViewsSitemap

sitemaps = {
    'static': StaticViewsSitemap
}

app_name = 'mysite'

handler404 = 'mysite.all_views.views_errors.error_404'
handler500 = 'mysite.all_views.views_errors.error_500'


def urlpatterns():
    return [
        path('', all_views.other_views.index, name='index'),
        path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
        path('Contact_me/', all_views.other_views.ContactMe, name='contact'),
        path('About/', all_views.other_views.Aboutme, name="about"),
        path('Supportme/', all_views.other_views.Supportme, name="support"),
        path('Sitemaps/', all_views.other_views.sitemaps),
        # PrivacyPolicy
        path('Privacy_policy/', all_views.other_views.PrivacyPolicy,
             name="PrivacyPolicy"),
    ]
