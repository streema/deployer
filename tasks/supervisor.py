from fabric.api import run, cd, env
from fabric.decorators import with_settings
from fabric.colors import green

from fabtools import supervisor, files

## TODO: use upload_template to prevent hardcoded
## supervisor configuration files
@with_settings(warn_only=True)
def setup():
    print(green('Setting up supervisor workers'))
    conf_dir = '{}/deploy/supervisor'.format(env.app_dir)
    with cd(conf_dir):
        output = run('ls')
        list_files = output.split()
        for file in list_files:
            files.symlink('{}/{}'.format(conf_dir, file), '/etc/supervisor/conf.d/', use_sudo=True)

    update_config()

def update_config():
    supervisor.update_config()

def reload_config():
    supervisor.reload_config()

def restart(component):
    update_config()
    supervisor.restart_process(component)

def stop(component):
    supervisor.stop_process(component)

def start(component):
    supervisor.start_process(component)
