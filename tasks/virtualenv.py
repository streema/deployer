from fabric.api import run, env
from fabric.decorators import with_settings
from fabric.context_managers import shell_env, cd 
from fabric.colors import red, green, yellow

from fabtools import require
from fabtools.python import virtualenv

from python import install_requirements
from git import deploy_code

@with_settings(warn_only=True)
def setup_virtualenv(python_version='', app_name='', app_dir='', repo_url=''):
    print(green("Setting up virtualenv on {}".format(app_dir)))

    print(green('Creating virtualenv'))
    if run("pyenv virtualenv {0} {1}-{0}".format(python_version, app_name)).failed:
        print(yellow("Virtualenv already exists"))

        install_requirements(app_name, python_version)
