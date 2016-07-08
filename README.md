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


