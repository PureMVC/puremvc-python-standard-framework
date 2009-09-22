from fabric.api import *

def clean():
    'remove local .pyc files'

    local("find ./src/ -name '*.pyc' -exec rm -rf {} \;")    
    local("find ./unittest/ -name '*.pyc' -exec rm -rf {} \;")    

def docs():
    'Build docs'

    local("rm -rf ./docs/*")
    local("epydoc --html --name 'PureMVC Python' ./src/puremvc -o ./docs/")

def test():
    'Run unit tests'
    setup()

    local("python ./unittest/main.py")
