from environs import Env

env = Env()

APPS = [
    'users',
    'merchandise',
    'orders',
    'tags',
    'events'
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
