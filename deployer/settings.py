from os import environ
from fabric.api import env

# Forward SSH agent
env.forward_agent = True

env.python_version = environ.get('APP_PYTHON_VERSION')

env.app_name = environ.get('APP_NAME')
env.app_dir = '/var/local/streema/{}'.format(environ.get('APP_NAME'))
env.repo_url = environ.get('APP_REPO_URL')
