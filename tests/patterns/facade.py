import unittest

import puremvc.interfaces
import puremvc.patterns.proxy
import puremvc.patterns.mediator
import puremvc.patterns.observer
import puremvc.patterns.facade
import utils.facade

class FacadeTest(unittest.TestCase):
    """FacadeTest: Test Facade Pattern"""
    
    def assertNotNone(self):
        """FacadeTest: Test instance not null"""
        fcde = puremvc.patterns.facade.Facade.getInstance()
        self.assertNotEqual(None, fcde) 

    def assertIFacade(self):
        """FacadeTest: Test instance implements IFacade"""
        fcde = puremvc.patterns.facade.Facade.getInstance()
        self.assertEqual(True, isinstance(fcde, puremvc.interfaces.IFacade))

    def testRegisterCommandAndSendNotification(self):
        """FacadeTest: Test registerCommand() and sendNotification()"""

        fcde = puremvc.patterns.facade.Facade.getInstance()
        fcde.registerCommand('FacadeTestNote', utils.facade.FacadeTestCommand)

        vo = utils.facade.FacadeTestVO(32)
        fcde.sendNotification('FacadeTestNote', vo)

        self.assertEqual(True, vo.result == 64)

    def testRegisterAndRemoveCommandAndSendNotification(self): 
        """FacadeTest: Test removeCommand() and subsequent sendNotification()"""
        fcde = puremvc.patterns.facade.Facade.getInstance()
        fcde.registerCommand('FacadeTestNote', utils.facade.FacadeTestCommand)
        fcde.removeCommand('FacadeTestNote')

        vo = utils.facade.FacadeTestVO(32)
        fcde.sendNotification('FacadeTestNote', vo)

        self.assertEqual(True, vo.result != 64)

    def testRegisterAndRetrieveProxy(self): 
        """FacadeTest: Test registerProxy() and retrieveProxy()"""
        fcde = puremvc.patterns.facade.Facade.getInstance()
        fcde.registerProxy(puremvc.patterns.proxy.Proxy('colors', ['red', 'green', 'blue']))
        pxy = fcde.retrieveProxy('colors')

        self.assertEqual(True, isinstance(pxy, puremvc.interfaces.IProxy))

        data = pxy.getData()

        self.assertEqual(True, data is not None)
        self.assertEqual(True, isinstance(data, list))
        self.assertEqual(True, len(data) == 3)
        self.assertEqual(True, data[0]  == 'red')
        self.assertEqual(True, data[1]  == 'green')
        self.assertEqual(True, data[2]  == 'blue')
           
    def testRegisterAndRemoveProxy(self): 
        """FacadeTest: Test registerProxy() and removeProxy()"""

        fcde = puremvc.patterns.facade.Facade.getInstance()
        pxy = puremvc.patterns.proxy.Proxy('sizes', ['7', '13', '21'])
        fcde.registerProxy(pxy)

        removedProxy = fcde.removeProxy('sizes')

        self.assertEqual(True, removedProxy.getProxyName() == 'sizes')

        pxy = fcde.retrieveProxy('sizes')

        self.assertEqual(True, pxy == None)

    def testRegisterRetrieveAndRemoveMediator(self): 
        """FacadeTest: Test registerMediator() retrieveMediator() and removeMediator()"""

        fcde = puremvc.patterns.facade.Facade.getInstance()
        fcde.registerMediator(puremvc.patterns.mediator.Mediator(puremvc.patterns.mediator.Mediator.NAME, object()))

        self.assertEqual(True, fcde.retrieveMediator(puremvc.patterns.mediator.Mediator.NAME) is not None)

        removedMediator = fcde.removeMediator(puremvc.patterns.mediator.Mediator.NAME)

        self.assertEqual(True, removedMediator.getMediatorName() == puremvc.patterns.mediator.Mediator.NAME)

        self.assertEqual(True, fcde.retrieveMediator(puremvc.patterns.mediator.Mediator.NAME) == None)

    def testHasProxy(self): 
        """FacadeTest: Test hasProxy()"""

        fcde = puremvc.patterns.facade.Facade.getInstance()
        fcde.registerProxy(puremvc.patterns.proxy.Proxy('hasProxyTest', [1,2,3]))

        self.assertEqual(True, fcde.hasProxy('hasProxyTest'))
        
        fcde.removeProxy('hasProxyTest')

        self.assertEqual(False, fcde.hasProxy('hasProxyTest'))

    def testHasMediator(self): 
        """FacadeTest: Test hasMediator()"""

        fcde = puremvc.patterns.facade.Facade.getInstance()
        fcde.registerMediator(puremvc.patterns.mediator.Mediator('facadeHasMediatorTest', object()))

        self.assertEqual(True, fcde.hasMediator('facadeHasMediatorTest'))

        fcde.removeMediator('facadeHasMediatorTest')

        self.assertEqual(False, fcde.hasMediator('facadeHasMediatorTest'))
            
    def testHasCommand(self): 
        """FacadeTest: Test hasCommand()"""    
        fcde = puremvc.patterns.facade.Facade.getInstance()
        fcde.registerCommand('facadeHasCommandTest', utils.facade.FacadeTestCommand)

        self.assertEqual(True, fcde.hasCommand('facadeHasCommandTest'))

        fcde.removeCommand('facadeHasCommandTest')

        self.assertEqual(False, fcde.hasCommand('facadeHasCommandTest'))
