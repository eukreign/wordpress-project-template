from os import getcwd, sep
from fabric.api import cd, run, env
from fabric.contrib.project import rsync_project

env.hosts = ['grafton2@graftonweb.com']

project = getcwd().split(sep)[-1]

def rsync():
    rsync_project(
        remote_dir='www',
        exclude=['wordpress',
                 'wp-config.php', 'local.wp-config.php',
                 '.hg', '.idea', 'error_log', '.hgignore'],
        extra_opts='--chmod=go-w'
    )

def push():
    rsync()
    with cd('www/'+project):
        run('cp production.wp-config.php wp-config.php')
