from os import environ, getcwd
from os.path import join

from fabric.api import env

from dotenv import load_dotenv

# Load .env file
dotenv_path = join(getcwd(), '.env')
load_dotenv(dotenv_path)

# Forward SSH agent
env.forward_agent = True

env.python_version = environ.get('APP_PYTHON_VERSION')

env.app_name = environ.get('APP_NAME')
env.app_dir = '/var/local/apps/{}'.format(environ.get('APP_NAME'))
env.repo_url = environ.get('APP_REPO_URL')
