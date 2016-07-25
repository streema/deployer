from fabric.api import run
from fabric.decorators import with_settings
from fabric.colors import green, yellow

from deployer.tasks.requirements import install_requirements

@with_settings(warn_only=True)
def setup_virtualenv(python_version='', app_name='', app_dir='', repo_url=''):
    print(green("Setting up virtualenv on {}".format(app_dir)))

    print(green('Creating virtualenv'))
    if run("pyenv virtualenv {0} {1}-{0}".format(python_version, app_name)).failed:
        print(yellow("Virtualenv already exists"))

        install_requirements(app_name, python_version)
