from fabric.api import sudo
from fabtools import service

def stop(component):
    service.stop(component)

def start(component):
    service.start(component)

def restart(component):
    if service.is_running(component):
        service.restart(component)
    else:
        service.start(component)

def reload(component):
    service.reload(component)

def upstart_reload():
    sudo('initctl reload-configuration')
