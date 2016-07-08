from fabric.api import run, env
from fabric.decorators import with_settings
from fabric.context_managers import shell_env 
from fabric.colors import red, green, yellow


@with_settings(warn_only=True)
def install_python(version=''):
    print(green("Installing python {}".format(version)))
    with shell_env(HOME='/home/' + env.user, PATH="/home/" + env.user + "/.pyenv/bin:$PATH"):
        run("pyenv install -s {}".format(version))
