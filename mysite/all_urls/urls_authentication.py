from .. import all_views
from django.urls import path


def urlpatterns():
    urlpatterns = [
        path('login/', all_views.views_authentication.Login, name="Login"),
        path('signin/', all_views.views_authentication.Signin, name="Signin"),
        path('logout/', all_views.views_authentication.Logout, name="Logout"),
    ]
    return urlpatterns
