from fabric.decorators import with_settings
from fabric.colors import green

from fabtools import require
from fabtools import git

@with_settings(warn_only=True)
def clone_repo(repo_url='', app_dir='', user=''):
    print(green('Cloning github repo {}'.format(repo_url)))
    require.git.working_copy(repo_url, app_dir, user=user)

@with_settings(warn_only=True)
def deploy_code(repo_url='', app_dir='', user='', remote='origin', branch='master'):

    raw_branch = ''
    if '/' in branch:
        remote, raw_branch = branch.split('/')

    print(green('Fetching {}'.format(remote)))
    git.fetch(app_dir, remote=remote)

    print(green('Checking out {}'.format(branch)))
    git.checkout(app_dir, branch=branch)

    print(green('Pulling updates from {}'.format(branch)))
    if raw_branch:
        git.pull(app_dir, remote=remote, branch=raw_branch)
    else:
        git.pull(app_dir, remote=remote, branch=branch)

@with_settings(warn_only=True)
def add_remote(remote_url='', repo_name='', app_dir=''):
    print(green('Adding new remote: {}'.format(repo_name)))
    git.add_remote(app_dir, repo_name, remote_url)
