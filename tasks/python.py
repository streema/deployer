from fabric.api import env

from fabric.decorators import with_settings
from fabric.context_managers import shell_env, cd 

from fabtools import require
from fabtools.python import virtualenv

@with_settings(warn_only=True)
def install_requirements(app_name='', python_version=''):
    with virtualenv('/home/deploy/.pyenv/versions/{0}-{1}'.format(app_name, python_version)):
        require.python.requirements('requirements.txt')
