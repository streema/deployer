from os import environ, getcwd
from os.path import join

from fabric.api import env

from dotenv import load_dotenv

env.env_file = environ.get('ENV_FILE', './config/settings/.env')

# Load .env file
dotenv_path = join(getcwd(), env.env_file)
load_dotenv(dotenv_path)

# Forward SSH agent
env.forward_agent = True

env.python_version = environ.get('APP_PYTHON_VERSION')

env.app_name = environ.get('APP_NAME')
env.app_dir = '{}/{}'.format(environ.get('INSTALL_DIR'), environ.get('APP_NAME'))
env.repo_url = environ.get('APP_REPO_URL')

env.supervisor_services = environ.get('SUPERVISOR_SERVICES', '').split(',')
env.upstart_services = environ.get('UPSTART_SERVICES', '').split(',')
