# settings/production.py

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j89c9cyjiw6h0gtp_0&-w+m8aau!#z7#_k+8d^surl_y*m+&s^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['http://3.112.205.117/']


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
				'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bee', #　作成したデータベース名
        'USER': 'admin', # ログインユーザー名
        'HOST': 'bee.c2optcdvbqga.ap-northeast-1.rds.amazonaws.com',
        'PORT': '3306',
        'PASSWORD': 'admin000',
    }
}