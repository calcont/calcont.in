from basicsite.settings.base import *
import os

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles")
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '475883331625-q7vvbr7ovpjs7lhjr0rfdoil53gd1r69.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'y8FZoB0bV4DceEm6pFg1mmpe'