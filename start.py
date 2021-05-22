from gunicorn.app.base import BaseApplication
from uvicorn.workers import UvicornWorker
from environs import Env
import multiprocessing
import uvicorn
import django
from django.core.management import call_command
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventz.settings')
APPLICATION = 'eventz.asgi:application'
django.setup()

env = Env()
DEPLOY_ENV = env.str('DEPLOY_ENV', 'development')
HOST = env.str('HOST', '127.0.0.1')
PORT = env.int('PORT', '8000')
LOG_LEVEL = env.str('LOG_LEVEL', 'info')


class EventzApp(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


class EventzAppWorker(UvicornWorker):
    CONFIG_KWARGS = {"loop": "uvloop", "http": "httptools"}


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


def run_dev():
    uvicorn.run(APPLICATION, host=HOST, port=PORT, log_level=LOG_LEVEL, loop='uvloop', http='httptools', reload=True)


def run_production():
    options = {
        'bind': '%s:%s' % (HOST, PORT),
        'workers': number_of_workers(),
        'loglevel': LOG_LEVEL,
        'worker_class': "start.EventzAppWorker"
    }
    EventzApp(APPLICATION, options).run()

def run_commands():
    call_command('migrate')
    call_command('collectstatic', '--no-input')


if __name__ == "__main__":
    # run_commands()
    if DEPLOY_ENV == 'development':
        print("Running development mode:")
        run_dev()
    else:
        print("Running production mode:")
        run_production()
