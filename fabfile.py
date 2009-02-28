def setup():
    pass

def clean():
    'remove local .pyc files'

    local("find ./src/ -name '*.pyc' -exec rm -rf {} \;")    
    local("find ./unittest/ -name '*.pyc' -exec rm -rf {} \;")    

def docs():
    'Build epydocs'
    setup()

    local("epydoc --html ./src/puremvc -o ./epydoc/")


def test():
    'Run unit tests'
    setup()

    local("python ./unittest/main.py")
