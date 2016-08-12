# Streema Deployer

Base deploy tool using [Fabric](http://www.fabfile.org/)

Directory structure
```
├── __init__.py
├── envs.py             # App environments such as staging/prod/etc go here
├── fabfile.py          # Main fabfile
├── requirements.txt 
├── settings.py         # App and fabric settings go here
└── tasks               # Task directory, create any task and call it from fabfile.py
    ├── __init__.py
    ├── git.py
    ├── pyenv.py
    ├── python.py
    └── virtualenv.py
```

# Configuration

You must have a `.env` file with the required variables on your app's root directory that is using deployer

# Env Variables 
## Required env variables
`PRODUCTION_SERVERS=<ip|domain>,<ip|domain>...`
   A list of IPs and/or domains of production servers

`APP_REPO_URL=git@github.com:streema/<project>.git`
   Application repository URL that is going to be deployed

`APP_PYTHON_VERSION=<python.version>`
   Python version to use on your app

`APP_NAME=<application name>`
   Application name, this is used mostly in combination with `APP_PYTHON_VERSION` to generate different virtual environments. This way you can have the same application running on different python versions.

## Optional env variables
`STAGING_SERVERS=<ip|domain>,<ip|domain>,...`
   You need this one in order to use `fab staging <command>`

## Example `.env` file
```
STAGING_SERVERS=192.168.1.210
PRODUCTION_SERVERS=production1.app.com,200.33.221.257
APP_REPO_URL=git@github.com:streema/deployer.git
APP_PYTHON_VERSION=2.7
APP_NAME=deployer
```

# Commands

#### Add a new remote repository

`fab production git_remote_add:<remoteurl>,<name>`

example:

`fab production git_remote_add:git@github.com:n0n0x/deployer.git,n0n0x`

#### Deploy master branch
`fab production deploy`

#### Deploy other branch

`fab production deploy:remotename/branch`

example:

`fab production deploy:n0n0x/fixes` will deploy `fixes` branch from remote `n0n0x`

