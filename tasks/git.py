from fabric.decorators import with_settings
from fabtools import require
from fabric.colors import green

@with_settings(warn_only=True)
def deploy_code(repo_url='', app_dir='', user='', update=False):
        print(green('Cloning github repo'))
        require.git.working_copy(repo_url, app_dir, user=user, update=update)
