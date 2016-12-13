from fabric.api import env, task
from fabric.state import output
from fabric.context_managers import shell_env, cd 

#output.stdout = False

from deployer.tasks.pyenv import install_python
from deployer.tasks.virtualenv import setup_virtualenv
from deployer.tasks.git import clone_repo, deploy_code, add_remote
from deployer.tasks.requirements import install_requirements

from deployer.envs import staging, production
from deployer.settings import *


@task
def setup_environment():
    with shell_env(HOME='/home/' + env.user, PATH="/home/" + env.user + "/.pyenv/bin:$PATH"):
        install_python(version=env.python_version)
        clone_repo(env.repo_url, env.app_dir, env.user)
        with cd(env.app_dir):
            setup_virtualenv(env.python_version, env.app_name, env.app_dir, env.repo_url)

@task
def deploy(branch='master'):
    with shell_env(HOME='/home/' + env.user, PATH="/home/" + env.user + "/.pyenv/bin:$PATH"):
        with cd(env.app_dir):
            deploy_code(env.repo_url, env.app_dir, env.user, branch=branch)
            install_requirements(env.app_name, env.python_version)

@task
def git_remote_add(remote_url, repo_name):
    with shell_env(HOME='/home/' + env.user, PATH="/home/" + env.user + "/.pyenv/bin:$PATH"):
        with cd(env.app_dir):
            add_remote(remote_url, repo_name, env.app_dir)
