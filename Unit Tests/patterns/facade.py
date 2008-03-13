import unittest

import org.puremvc.python.interfaces
import org.puremvc.python.patterns.proxy
import org.puremvc.python.patterns.mediator
import org.puremvc.python.patterns.observer
import org.puremvc.python.patterns.facade
import utils.facade

class FacadeTest(unittest.TestCase):
	"""FacadeTest: Test Facade Pattern"""
	
	def assertNotNone(self):
		"""FacadeTest: Test instance not null"""
		fcde = org.puremvc.python.patterns.facade.Facade.getInstance()
   		self.assertNotEqual(None, fcde) 

	def assertIFacade(self):
		"""FacadeTest: Test instance implements IFacade"""
		fcde = org.puremvc.python.patterns.facade.Facade.getInstance()
   		self.assertEqual(True, isinstance(fcde, org.puremvc.python.interfaces.IFacade))

  	def testRegisterCommandAndSendNotification(self):
  		"""FacadeTest: Test registerCommand() and sendNotification()"""

		fcde = org.puremvc.python.patterns.facade.Facade.getInstance()
		fcde.registerCommand('FacadeTestNote', utils.facade.FacadeTestCommand)

		vo = utils.facade.FacadeTestVO(32)
		fcde.sendNotification('FacadeTestNote', vo)

		self.assertEqual(True, vo.result == 64)

	def testRegisterAndRemoveCommandAndSendNotification(self): 
		"""FacadeTest: Test removeCommand() and subsequent sendNotification()"""
		fcde = org.puremvc.python.patterns.facade.Facade.getInstance()
		fcde.registerCommand('FacadeTestNote', utils.facade.FacadeTestCommand)
		fcde.removeCommand('FacadeTestNote')

		vo = utils.facade.FacadeTestVO(32)
		fcde.sendNotification('FacadeTestNote', vo)

		self.assertEqual(True, vo.result != 64)

  	def testRegisterAndRetrieveProxy(self): 
  		"""FacadeTest: Test registerProxy() and retrieveProxy()"""
		fcde = org.puremvc.python.patterns.facade.Facade.getInstance()
		fcde.registerProxy(org.puremvc.python.patterns.proxy.Proxy('colors', ['red', 'green', 'blue']))
		pxy = fcde.retrieveProxy('colors')

		self.assertEqual(True, isinstance(pxy, org.puremvc.python.interfaces.IProxy))

		data = pxy.getData()

		self.assertEqual(True, data is not None)
		self.assertEqual(True, isinstance(data, list))
		self.assertEqual(True, len(data) == 3)
		self.assertEqual(True, data[0]  == 'red')
		self.assertEqual(True, data[1]  == 'green')
		self.assertEqual(True, data[2]  == 'blue')
   		
  	def testRegisterAndRemoveProxy(self): 
  		"""FacadeTest: Test registerProxy() and removeProxy()"""

		fcde = org.puremvc.python.patterns.facade.Facade.getInstance()
		pxy = org.puremvc.python.patterns.proxy.Proxy('sizes', ['7', '13', '21'])
		fcde.registerProxy(pxy)

		removedProxy = fcde.removeProxy('sizes')

		self.assertEqual(True, removedProxy.getProxyName() == 'sizes')

		pxy = fcde.retrieveProxy('sizes')

		self.assertEqual(True, pxy == None)

 	def testRegisterRetrieveAndRemoveMediator(self): 
  		"""FacadeTest: Test registerMediator() retrieveMediator() and removeMediator()"""

		fcde = org.puremvc.python.patterns.facade.Facade.getInstance()
		fcde.registerMediator(org.puremvc.python.patterns.mediator.Mediator(org.puremvc.python.patterns.mediator.Mediator.NAME, object()))

		self.assertEqual(True, fcde.retrieveMediator(org.puremvc.python.patterns.mediator.Mediator.NAME) is not None)

		removedMediator = fcde.removeMediator(org.puremvc.python.patterns.mediator.Mediator.NAME)

		self.assertEqual(True, removedMediator.getMediatorName() == org.puremvc.python.patterns.mediator.Mediator.NAME)

		self.assertEqual(True, fcde.retrieveMediator(org.puremvc.python.patterns.mediator.Mediator.NAME) == None)

 	def testHasProxy(self): 
  		"""FacadeTest: Test hasProxy()"""

		fcde = org.puremvc.python.patterns.facade.Facade.getInstance()
		fcde.registerProxy(org.puremvc.python.patterns.proxy.Proxy('hasProxyTest', [1,2,3]))

		self.assertEqual(True, fcde.hasProxy('hasProxyTest'))
		
		fcde.removeProxy('hasProxyTest')

		self.assertEqual(False, fcde.hasProxy('hasProxyTest'))

  	def testHasMediator(self): 
  		"""FacadeTest: Test hasMediator()"""

		fcde = org.puremvc.python.patterns.facade.Facade.getInstance()
		fcde.registerMediator(org.puremvc.python.patterns.mediator.Mediator('facadeHasMediatorTest', object()))

		self.assertEqual(True, fcde.hasMediator('facadeHasMediatorTest'))

		fcde.removeMediator('facadeHasMediatorTest')

		self.assertEqual(False, fcde.hasMediator('facadeHasMediatorTest'))
			
	def testHasCommand(self): 
  		"""FacadeTest: Test hasCommand()"""	
		fcde = org.puremvc.python.patterns.facade.Facade.getInstance()
		fcde.registerCommand('facadeHasCommandTest', utils.facade.FacadeTestCommand)

		self.assertEqual(True, fcde.hasCommand('facadeHasCommandTest'))

		fcde.removeCommand('facadeHasCommandTest')

		self.assertEqual(False, fcde.hasCommand('facadeHasCommandTest'))
   			
   		