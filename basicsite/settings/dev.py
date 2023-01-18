from basicsite.settings.base import *
import os

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+%1e1)rzsn_c%3cm8b5y_+su3!90gu6#efpy38pob%^5_1_8_+'

ALLOWED_HOSTS = ['127.0.0.1']

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles")
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '475883331625-q7vvbr7ovpjs7lhjr0rfdoil53gd1r69.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'y8FZoB0bV4DceEm6pFg1mmpe'