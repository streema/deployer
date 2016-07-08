from fabric.api import env
from fabric.state import output
from fabric.context_managers import shell_env, cd 

#output.stdout = False

from envs import production, staging
from tasks.pyenv import install_python
from tasks.virtualenv import setup_virtualenv
from tasks.git import deploy_code
from tasks.python import install_requirements 

from settings import *

def setup_environment():
    with shell_env(HOME='/home/' + env.user, PATH="/home/" + env.user + "/.pyenv/bin:$PATH"):
        with cd(env.app_dir):
            install_python(version=env.python_version)
            deploy_code(env.repo_url, env.app_dir, env.user)
            setup_virtualenv(env.python_version, env.app_name, env.app_dir, env.repo_url)


def deploy():
    with shell_env(HOME='/home/' + env.user, PATH="/home/" + env.user + "/.pyenv/bin:$PATH"):
        with cd(env.app_dir):
            deploy_code(env.repo_url, env.app_dir, env.user, update=True)
            install_requirements(env.app_name, env.python_version)
