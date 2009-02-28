import unittest
from core import controller,model,view
from patterns import command, facade, mediator, observer, proxy

if __name__ == '__main__':
    
    TestSuite = unittest.TestSuite()
    
    TestSuite.addTest(controller.ControllerTest("assertNotNone"))
    TestSuite.addTest(controller.ControllerTest("assertIController"))
    TestSuite.addTest(controller.ControllerTest("testRegisterAndExecuteCommand"))
    TestSuite.addTest(controller.ControllerTest("testRegisterAndRemoveCommand"))
    TestSuite.addTest(controller.ControllerTest("testHasCommand"))

    TestSuite.addTest(model.ModelTest("assertNotNone"))
    TestSuite.addTest(model.ModelTest("assertIModel"))
    TestSuite.addTest(model.ModelTest("testRegisterAndRetrieveProxy"))
    TestSuite.addTest(model.ModelTest("testRegisterAndRemoveProxy"))
    TestSuite.addTest(model.ModelTest("testHasProxy"))
    TestSuite.addTest(model.ModelTest("testOnRegisterAndOnRemove"))
    
    TestSuite.addTest(view.ViewTest("assertNotNone"))
    TestSuite.addTest(view.ViewTest("assertIView"))
    TestSuite.addTest(view.ViewTest("testRegisterAndNotifyObserver"))
    TestSuite.addTest(view.ViewTest("testRegisterAndRetrieveMediator"))
    TestSuite.addTest(view.ViewTest("testHasMediator"))
    TestSuite.addTest(view.ViewTest("testRegisterAndRemoveMediator"))
    TestSuite.addTest(view.ViewTest("testOnRegisterAndOnRemove"))
    TestSuite.addTest(view.ViewTest("testSuccessiveRegisterAndRemoveMediator"))
    TestSuite.addTest(view.ViewTest("testRemoveMediatorAndSubsequentNotify"))
    TestSuite.addTest(view.ViewTest("testRemoveOneOfTwoMediatorsAndSubsequentNotify"))
    TestSuite.addTest(view.ViewTest("testMediatorReregistration"))
    
    TestSuite.addTest(command.CommandTest("testMacroCommandExecute"))
    TestSuite.addTest(command.CommandTest("testSimpleCommandExecute"))
    
    TestSuite.addTest(facade.FacadeTest("assertNotNone"))
    TestSuite.addTest(facade.FacadeTest("assertIFacade"))
    TestSuite.addTest(facade.FacadeTest("testRegisterCommandAndSendNotification"))
    TestSuite.addTest(facade.FacadeTest("testRegisterAndRemoveCommandAndSendNotification"))
    TestSuite.addTest(facade.FacadeTest("testRegisterAndRetrieveProxy"))
    TestSuite.addTest(facade.FacadeTest("testRegisterAndRemoveProxy"))
    TestSuite.addTest(facade.FacadeTest("testRegisterRetrieveAndRemoveMediator"))
    TestSuite.addTest(facade.FacadeTest("testHasProxy"))
    TestSuite.addTest(facade.FacadeTest("testHasMediator"))
    TestSuite.addTest(facade.FacadeTest("testHasCommand"))
    
    TestSuite.addTest(mediator.MediatorTest("testNameAccessor"))
    TestSuite.addTest(mediator.MediatorTest("testViewAccessor"))
    
    TestSuite.addTest(observer.ObserverTest("testObserverAccessors"))
    TestSuite.addTest(observer.ObserverTest("testObserverConstructor"))
    TestSuite.addTest(observer.ObserverTest("testCompareNotifyContext"))
    TestSuite.addTest(observer.ObserverTest("testNameAccessors"))
    TestSuite.addTest(observer.ObserverTest("testBodyAccessors"))
    TestSuite.addTest(observer.ObserverTest("testConstructor"))
    
    TestSuite.addTest(proxy.ProxyTest("testNameAccessor"))
    TestSuite.addTest(proxy.ProxyTest("testDataAccessors"))
    TestSuite.addTest(proxy.ProxyTest("testConstructor"))
    
    unittest.TextTestRunner(verbosity=2).run(TestSuite)
