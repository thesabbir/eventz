from importlib import import_module

from environs import Env
import inspect
from django.contrib import admin

env = Env()

APPS = [
    'users',
    'merchandise',
    'orders',
    'tags',
    'events',
    'token_auth'
]

POSTGRES = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': env.str('POSTGRES_DB'),
    'USER': env.str('POSTGRES_USER'),
    'PASSWORD': env.str('POSTGRES_PASSWORD'),
    'HOST': env.str('POSTGRES_HOST'),
    'PORT': 5432,
}

USER_MODEL = 'users.UserModel'

