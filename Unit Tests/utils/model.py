import org.puremvc.python.patterns.proxy

class ModelTestProxy(org.puremvc.python.patterns.proxy.Proxy):
	NAME = 'ModelTestProxy'
	ON_REGISTER_CALLED = 'onRegister Called'
	ON_REMOVE_CALLED = 'onRemove Called'

	def __init__(self):
		org.puremvc.python.patterns.proxy.Proxy.__init__(self, ModelTestProxy.NAME, object())

	def onRegister(self):
		self.setData(ModelTestProxy.ON_REGISTER_CALLED)		

	def onRemove(self):
		self.setData(ModelTestProxy.ON_REMOVE_CALLED) 