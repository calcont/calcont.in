from basicsite.settings.base import *
import os
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ADMINS = [
    ('CalConT', 'calcont.in01@gmail.com'),
]

EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = ' postmaster@sandbox0c4d0d0425594b65865fb83a4b57c093.mailgun.org'
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

ALLOWED_HOSTS = ['127.0.0.1']

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles")
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '475883331625-q7vvbr7ovpjs7lhjr0rfdoil53gd1r69.apps.googleusercontent.com'# for development purpose
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'y8FZoB0bV4DceEm6pFg1mmpe'