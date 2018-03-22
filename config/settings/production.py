from .base import *
import os

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = [
    'utomica.co',
    'www.utomica.co',
    'monooki.herokuapp.com',
    'localhost'
]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

