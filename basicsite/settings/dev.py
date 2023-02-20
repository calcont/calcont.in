from basicsite.settings.base import *
import os
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles")
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '475883331625-q7vvbr7ovpjs7lhjr0rfdoil53gd1r69.apps.googleusercontent.com'# for development purpose
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'y8FZoB0bV4DceEm6pFg1mmpe'
