from fabric.api import env

def production():
    env.user = 'deploy'
    env.hosts = ['104.236.83.206']

def staging():
    env.user = 'deploy'
    env.hosts = ['104.236.83.206']
