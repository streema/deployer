import dotenv

from fabric.api import env, task
from fabric.state import output
from fabric.context_managers import shell_env, cd

#output.stdout = False

from deployer.settings import *
from deployer.envs import staging, production

from deployer.tasks import supervisor
from deployer.tasks.pyenv import install_python
from deployer.tasks.virtualenv import setup_virtualenv
from deployer.tasks.git import clone_repo, deploy_code, add_remote
from deployer.tasks.requirements import install_requirements
from deployer.tasks.envfile import envconf
from .tasks.supervisor import restart_all


@task
def setup_environment():
    with shell_env(HOME='/home/' + env.user, PATH="/home/" + env.user + "/.pyenv/bin:$PATH"):
        install_python(version=env.python_version)
        clone_repo(env.repo_url, env.app_dir, env.user)
        with cd(env.app_dir):
            setup_virtualenv(env.python_version, env.app_name, env.app_dir, env.repo_url)


@task
def deploy(branch='master', migrate=False):
    with shell_env(HOME='/home/' + env.user, PATH="/home/" + env.user + "/.pyenv/bin:$PATH"):
        with cd(env.app_dir):
            deploy_code(env.repo_url, env.app_dir, env.user, branch=branch)
            install_requirements(env.app_name, env.python_version)
            if env.restart_after_deploy:
                restart_all()


@task
def git_remote_add(remote_url, repo_name):
    with shell_env(HOME='/home/' + env.user, PATH="/home/" + env.user + "/.pyenv/bin:$PATH"):
        with cd(env.app_dir):
            add_remote(remote_url, repo_name, env.app_dir)


@task
def config(action=None, key=None, value=None):
    '''Manage project configuration via .env

    e.g: fab config:set,<key>,<value>
         fab config:get,<key>
         fab config:unset,<key>
         fab config:list
    '''
    with shell_env(HOME='/home/' + env.user, PATH="/home/" + env.user + "/.pyenv/bin:$PATH"):
        with cd(env.app_dir):
            envconf(action, key, value)
            restart_all()
