import os
from fabric.api import cd, run, local, env, get
from fabric.contrib.project import rsync_project

env.hosts = ['grafton2@graftonweb.com']

project = os.getcwd().split(os.sep)[-1]
path = os.path.join('www', project)

def rsync():
    rsync_project(
        remote_dir='www',
        exclude=['wordpress', 'fabfile.py',
                 'wp-config.php', 'local.wp-config.php',
                 '.hg', '.idea', 'error_log', '.hgignore'],
        extra_opts='--chmod=go-w'
    )

def push():
    rsync()
    with cd(path):
        run('cp production.wp-config.php wp-config.php')

def db():
    dbfile = 'database.sql'
    with cd(path):
        run('wp db export '+dbfile)
    get(os.path.join(path, dbfile), dbfile)
    local('wp db import '+dbfile)
