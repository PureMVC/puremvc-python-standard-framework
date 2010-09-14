import unittest

import puremvc.patterns.observer

class ObserverTest(unittest.TestCase):
    """ObserverTest: Test Observer Pattern"""
    
    __observerTestVar = None

    def __observerTestMethod(self,note):
        self.__observerTestVar = note.getBody()

    def testObserverAccessors(self):
        """ObserverTest: Test Observer Accessors"""

        obsrvr = puremvc.patterns.observer.Observer(None,None)
        obsrvr.setNotifyContext(self)
      
        obsrvr.setNotifyMethod(self.__observerTestMethod)

        note = puremvc.patterns.observer.Notification('ObserverTestNote',10)
        obsrvr.notifyObserver(note)
        
        self.assertEqual(True, self.__observerTestVar == 10)

    def testObserverConstructor(self): 
        """ObserverTest: Test Observer Constructor"""    

        obsrvr = puremvc.patterns.observer.Observer(self.__observerTestMethod,self)

        note = puremvc.patterns.observer.Notification('ObserverTestNote',5)
        obsrvr.notifyObserver(note)
         
        self.assertEqual(True, self.__observerTestVar == 5)
         
    def testCompareNotifyContext(self): 
        """ObserverTest: Test compareNotifyContext()"""    

        obsrvr = puremvc.patterns.observer.Observer(self.__observerTestMethod, self)

        negTestObj = object()
      
        self.assertEqual(False, obsrvr.compareNotifyContext(negTestObj))
        self.assertEqual(True, obsrvr.compareNotifyContext(self))

    def testNameAccessors(self): 
        """NotificationTest: Test Name Accessors"""
    
        note = puremvc.patterns.observer.Notification('TestNote')

        self.assertEqual(True, note.getName() == 'TestNote')
         
    def testBodyAccessors(self): 
        """NotificationTest: Test Body Accessors"""

        note = puremvc.patterns.observer.Notification(None)
        note.setBody(5)

        self.assertEqual(True, note.getBody() == 5)
         
    def testConstructor(self): 
        """NotificationTest: Test Constructor"""

        note = puremvc.patterns.observer.Notification('TestNote',5,'TestNoteType')

        self.assertEqual(True, note.getName() == 'TestNote')
        self.assertEqual(True, note.getBody() == 5)
        self.assertEqual(True, note.getType() == 'TestNoteType')
