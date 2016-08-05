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

## Required env variables
```
PRODUCTION_SERVERS=ip,ip,... or STAGING_SERVERS=ip,ip,...
APP_REPO_URL=git@github.com:streema/<project>.git
APP_PYTHON_VERSION=<python.version>
APP_NAME=<application name>
```

#### Example
```
PRODUCTION_SERVERS=127.0.0.1
APP_REPO_URL=git@github.com:streema/deployer.git
APP_PYTHON_VERSION=2.7
APP_NAME=deployer
```


## Commands

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

