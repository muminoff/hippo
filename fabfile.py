from fabric import colors
from fabric.api import task
from fabric.api import env
from fabric.api import run
from fabric.api import cd


env.hosts = ['hippo.uz']
env.user = 'hippo'
env.key_filename = 'secrets/ssh_keys/hippo.pem'


GITHUB = 'git@github.com:muminoff/hippo.git'
ROOT = '/home/hippo/'
CODE_ROOT = '%s/hippo' % ROOT
LOCAL_SETTINGS = '%s/hippo/settings/production.py' % CODE_ROOT
GUNICORN = '/usr/local/bin/gunicorn'


@task
def git_pull():
    with cd(CODE_ROOT):
        run('git pull origin master')


@task
def install_requirements():
    print(colors.cyan('Installing requirements...', bold=True))
    with cd(CODE_ROOT):
        run('pip install -U -r requirements.txt')
        run('pip install -e .')


@task
def deploy():
    """Deploy code to production"""
    print(colors.cyan('Deploying...', bold=True))
    with cd(CODE_ROOT):
        run('git pull origin develop')
        clear_cache()
        run('find . -name "*.pyc" -delete')
        restart()


@task
def clear_cache():
    with cd(CODE_ROOT):
        run('redis-cli -n 1 flushdb')


@task
def restart():
    with cd(CODE_ROOT):
        run('supervisorctl -c deploy/supervisord.conf shutdown')
        run('kill -9 `pgrep gunicorn|xargs`')
        run('supervisord -c deploy/supervisord.conf')
