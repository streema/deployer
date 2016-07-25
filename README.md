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

## Commands

#### Add a new remote repository

`fab production git_add_remote:<remoteurl>,<name>`

example:

`fab production git_add_remote:git@github.com:n0n0x/deployer.git,n0n0x`

#### Deploy master branch
`fab production deploy`

#### Deploy other branch

`fab production deploy:remotename/branch`

example:

`fab production deploy:n0n0x/fixes` will deploy `fixes` branch from remote `n0n0x`

