from pathlib import Path

SECRET_KEY = 'djan24wrh4w5i6g6,vk5rjrju67duj7l3j$726jl9s=r7q$2hpiska'

DEBUG = False

ALLOWED_HOSTS = ['176.124.199.217', 'testoza.ru']

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangopolls',
        'USER': 'djangopolls_admin',
        'PASSWORD': 'bashmachok',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}