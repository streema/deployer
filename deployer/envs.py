from os import environ
from fabric.api import env, task

@task
def production():
    env.user = 'deploy'
    env.environment = 'production'
    env.hosts = environ.get('PRODUCTION_SERVERS').split(',')

@task
def staging():
    env.user = 'deploy'
    env.environment = 'staging'
    env.hosts = environ.get('STAGING_SERVERS').split(',')
