import org.puremvc.python.patterns.command

class ControllerTestCommand(org.puremvc.python.patterns.command.SimpleCommand):
	
	def execute(self, note):
		vo = note.getBody()
		vo.result = 2 * vo.input;

class ControllerTestVO(object):
	
	input = 0
	result = 0
	
	def __init__(self, num=0):
		self.input = num