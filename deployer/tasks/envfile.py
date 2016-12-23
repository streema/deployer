import dotenv

from fabric.api import task, run, env
from fabric.decorators import with_settings
from fabric.colors import green, yellow

from fabtools.python import virtualenv

@task
@with_settings(warn_only=True)
def envconf(action=None, key=None, value=None):
    '''Manage project configuration via .env

    e.g: fab config:set,<key>,<value>
         fab config:get,<key>
         fab config:unset,<key>
         fab config:list
    '''
    with virtualenv('/home/deploy/.pyenv/versions/{0}-{1}'.format(env.app_name, env.python_version)):
        run('touch %(env_file)s' % env)
        command = dotenv.get_cli_string(env.env_file, action, key, value)
        run(command)
