import puremvc.patterns.command

class FacadeTestCommand(puremvc.patterns.command.SimpleCommand):
    def execute(self,note):
        vo = note.getBody()
        vo.result = 2 * vo.input;

class FacadeTestVO(object):
    
    input = None
    result = None
    
    def __init__(self,input):
        self.input = input
