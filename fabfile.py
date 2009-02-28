"""
Usage:

fab test
fab docs
"""

def setup():
    pass

def clean():
    'remove local .pyc files'
    local("find ./src/ -name '*.pyc' -exec rm -rf {} \;")    
    local("find ./Unit\ Tests/ -name '*.pyc' -exec rm -rf {} \;")    

def docs():
    'Build epydocs'
    setup()

    local("rm -rf ./epydoc")
    local("epydoc --html src/puremvc -o epydoc/")


def test():
    'Run unit tests'
    setup()

    local("python Unit\ Tests/main.py")
