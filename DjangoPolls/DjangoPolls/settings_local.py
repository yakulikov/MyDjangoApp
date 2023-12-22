from pathlib import Path

SECRET_KEY = 'djan24wrh4w5i6g6,vk5rjrju67duj7l3j$726jl9s=r7q$2hpiska'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}