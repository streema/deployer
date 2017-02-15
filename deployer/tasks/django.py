from fabric.api import run, runs_once
from fabric.decorators import with_settings

from fabtools import require
from fabtools.python import virtualenv

@with_settings(warn_only=True)
def collectstatic(app_name='', python_version=''):
    with virtualenv('/home/deploy/.pyenv/versions/{0}-{1}'.format(app_name, python_version)):
        run('python manage.py collectstatic -v0 --noinput')

@runs_once
@with_settings(warn_only=True)
def migrate(app_name='', python_version=''):
    with virtualenv('/home/deploy/.pyenv/versions/{0}-{1}'.format(app_name, python_version)):
        run('python manage.py migrate')
