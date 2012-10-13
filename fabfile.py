from fabric.api import *


def install():
    local("python ./setup.py clean")
    local("python ./setup.py install")


def clean():
    'remove local .pyc files'

    local("find ./src/ -name '*.pyc' -exec rm -rf {} \;")
    local("find ./tests/ -name '*.pyc' -exec rm -rf {} \;")


def docs():
    'Build docs'

    local("rm -rf ./docs/*")
    local("epydoc -v --html --name 'PureMVC Python' ./src/puremvc -o ./docs/")


def test():
    'Run unit tests'
    local("python ./tests/main.py")
