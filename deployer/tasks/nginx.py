from fabric.api import run, cd, env
from fabric.decorators import with_settings
from fabric.colors import green

from fabtools import service, files

## TODO: use upload_template to prevent hardcoded
## supervisor configuration files

service_name='nginx'

@with_settings(warn_only=True)
def setup():
    print(green('Setting up nginx config'))
    conf_dir = '{}/deploy/nginx'.format(env.app_dir)
    with cd(conf_dir):
        output = run('ls')
        list_files = output.split()
        for file in list_files:
            files.symlink('{}/{}'.format(conf_dir, file), '/etc/nginx/sites-enabled/', use_sudo=True)

    restart()

@with_settings(warn_only=True)
def stop():
    service.stop(service_name)

def start():
    service.start(service_name)

def reload_config():
    service.reload(service_name)

def restart():
    service.restart(service_name)

