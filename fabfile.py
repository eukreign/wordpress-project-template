from uuid import uuid4
from os import getcwd
from getpass import getuser
from os.path import join, exists
from fabric.api import local, lcd, prompt, env, abort

def create():
    #local("git submodule init")
    #local("git submodule update")

    prompt("Project Title:", "project_title", validate=nonempty)
    prompt("Project Name:", "project_name",
            clean(env.project_title), nonempty)
    prompt("Project URL:", "project_url",
            env.project_name+'.com', nonempty)
    prompt("Project User:", "project_user",
            getuser(), nonempty)

    path = join('../', env.project_name)
    if exists(path): abort("Project alread exists: "+path)

    local("cp -r %s %s" % (getcwd(), path))

    with lcd(path):
        themes = 'wp-content/themes/'
        theme_tpl = join(themes,'wordpress-theme-template')
        theme     = join(themes,env.project_name)

        local("mv %s %s" % (theme_tpl, theme))

        do_string_replacement([
            '.htaccess',
            'hgrc',
            'create.sh',
            'local.wp-config.php',
            'production.wp-config.php',
            'wp-cli.yml',
            join(theme, 'style.css')
        ])

        local("rm -rf .git")
        local("rm -rf "+join(theme, '.git'))
        local("rm wp-config-sample.php")
        local("rm .gitignore")
        local("rm .gitmodules")
        local("rm "+join(theme, '.gitignore'))
        local("rm "+join(theme, '.editorconfig'))

        local("hg init")
        local("mv hgrc .hg/")
        local("hg add .")
        local("hg commit -m'initial import'")

        local("cp local.wp-config.php wp-config.php")

def clean(t):
    return t.strip().lower().replace(' ','')

def nonempty(v):
    if len(v.strip())==0:
        raise "Cannot be empty."
    return v.strip()

def do_string_replacement(files):
    tplvars = {
        'Title': env.project_title,
        'Name': env.project_name,
        'URL': env.project_url,
        'User': env.project_user
    }
    tplvars.update([('Random Key %s'%i, uuid4()) for i in range(1,10)])
    sed = ';'.join([r's/\[Project %s\]/%s/g'%(key,val)
                    for key,val in tplvars.items()])
    for tpl in files:
        local(r'sed -i -e "%s" %s' % (sed, tpl))
