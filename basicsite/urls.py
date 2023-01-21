"""basicsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from mysite.sitemaps import StaticViewsSitemap
sitemaps = {
    'static': StaticViewsSitemap
}
urlpatterns = [
    path('calcont-admin/', admin.site.urls),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
    path('', include("mysite.all_urls")),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt",
         content_type='text/plain')),
    path('ads.txt/', TemplateView.as_view(template_name="ads.txt",
         content_type='text/plain')),
    path('.well-known/brave-rewards-verification.txt/', TemplateView.as_view(
        template_name=".well-known/brave-rewards-verification.txt", content_type='text/plain')),

    # path('analyze', views.analyze,name='analyze'),


]
