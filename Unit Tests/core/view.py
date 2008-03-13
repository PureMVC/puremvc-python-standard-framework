import unittest
	
import org.puremvc.python.interfaces
import org.puremvc.python.patterns.observer
import org.puremvc.python.patterns.proxy
import org.puremvc.python.patterns.mediator
import org.puremvc.python.core
import utils.view

class ViewTest(unittest.TestCase):
	"""ViewTest: Test View Singleton"""
	
	lastNotification = None
	onRegisterCalled = False
	onRemoveCalled = False

	NOTE1 = "note1"
	NOTE2 = "note2"
	NOTE3 = "note3"

	def __cleanup(self):
		org.puremvc.python.core.View.getInstance().removeMediator(utils.view.ViewTestMediator.NAME)
		org.puremvc.python.core.View.getInstance().removeMediator(utils.view.ViewTestMediator2.NAME)
		org.puremvc.python.core.View.getInstance().removeMediator(utils.view.ViewTestMediator3.NAME)
		org.puremvc.python.core.View.getInstance().removeMediator(utils.view.ViewTestMediator4.NAME)
	
	def assertNotNone(self):
		"""ViewTest: Test instance not null"""
		view = org.puremvc.python.core.View.getInstance()
		self.assertNotEqual(None, view) 

	def assertIView(self):
		"""ViewTest: Test instance implements IView"""
		view = org.puremvc.python.core.View.getInstance()
		self.assertEqual(True, isinstance(view, org.puremvc.python.interfaces.IView))

	def testRegisterAndNotifyObserver(self):
		"""ViewTest: Test registerObserver() and notifyObservers()"""
		
		self.viewTestVar = 0
		def viewTestMethod(note):
			self.viewTestVar = note.getBody()
		
		view = org.puremvc.python.core.View.getInstance()
		obsvr = org.puremvc.python.patterns.observer.Observer(viewTestMethod, self)
		view.registerObserver(utils.view.ViewTestNote.NAME, obsvr)
		
		note = utils.view.ViewTestNote.create(10)
		view.notifyObservers(note)
		
		self.assertEqual(True, self.viewTestVar == 10)

	def testRegisterAndRetrieveMediator(self):
		"""ViewTest: Test registerMediator() and retrieveMediator()"""
		view = org.puremvc.python.core.View.getInstance()

		viewTestMediator = utils.view.ViewTestMediator(self)
		view.registerMediator(viewTestMediator)
		
		mediator = view.retrieveMediator(utils.view.ViewTestMediator.NAME)
			
		self.assertEqual(True, isinstance(mediator, utils.view.ViewTestMediator))
		self.__cleanup()
			
	def testHasMediator(self):
		"""ViewTest: Test hasMediator()"""
		view = org.puremvc.python.core.View.getInstance()
		meditr = org.puremvc.python.patterns.mediator.Mediator('hasMediatorTest', self)
		view.registerMediator(meditr)

		self.assertEqual(True, view.hasMediator('hasMediatorTest'))

		view.removeMediator('hasMediatorTest')

		self.assertEqual(False, view.hasMediator('hasMediatorTest'))
		self.__cleanup()

	def testRegisterAndRemoveMediator(self):
		"""ViewTest: Test registerMediator() and removeMediator()"""
		view = org.puremvc.python.core.View.getInstance()

		meditr = org.puremvc.python.patterns.mediator.Mediator('testing', self)
		view.registerMediator(meditr)

		removedMediator = view.removeMediator('testing')

		self.assertEqual(True, removedMediator.getMediatorName() == 'testing')

		self.assertEqual(True, view.retrieveMediator('testing') == None)
		self.__cleanup()

	def testOnRegisterAndOnRemove(self):
		"""ViewTest: Test onRegsiter() and onRemove()"""
		view = org.puremvc.python.core.View.getInstance()

		mediator = utils.view.ViewTestMediator4(self)
		view.registerMediator(mediator)

		self.assertEqual(True, self.onRegisterCalled)

		view.removeMediator(utils.view.ViewTestMediator4.NAME)

		self.assertEqual(True, self.onRemoveCalled)
		self.__cleanup()


	def testSuccessiveRegisterAndRemoveMediator(self):
		"""ViewTest: Test Successive registerMediator() and removeMediator()"""
		view = org.puremvc.python.core.View.getInstance()

		view.registerMediator(utils.view.ViewTestMediator(self))
	
		self.assertEqual(True, isinstance(view.retrieveMediator(utils.view.ViewTestMediator.NAME), utils.view.ViewTestMediator))

		view.removeMediator(utils.view.ViewTestMediator.NAME)
		
		self.assertEqual(True, view.retrieveMediator(utils.view.ViewTestMediator.NAME) == None)
	
		self.assertEqual(True, view.removeMediator(utils.view.ViewTestMediator.NAME) == None)

		view.registerMediator(utils.view.ViewTestMediator(self))
	
		self.assertEqual(True, isinstance(view.retrieveMediator(utils.view.ViewTestMediator.NAME), utils.view.ViewTestMediator))

		view.removeMediator(utils.view.ViewTestMediator.NAME)
			
		self.assertEqual(True, view.retrieveMediator(utils.view.ViewTestMediator.NAME) == None)

		self.__cleanup()									
	
	def testRemoveMediatorAndSubsequentNotify(self): 
		"""ViewTest: Test removeMediator() and subsequent nofity()"""

		view = org.puremvc.python.core.View.getInstance()
	
		view.registerMediator(utils.view.ViewTestMediator2(self))
	
		view.notifyObservers(org.puremvc.python.patterns.observer.Notification(self.NOTE1))
		self.assertEqual(True, self.lastNotification == self.NOTE1)

		view.notifyObservers(org.puremvc.python.patterns.observer.Notification(self.NOTE2))
		self.assertEqual(True, self.lastNotification == self.NOTE2)

		view.removeMediator(utils.view.ViewTestMediator2.NAME)
		
		self.assertEqual(True, view.retrieveMediator(utils.view.ViewTestMediator2.NAME) == None)

		self.lastNotification = None
	
		view.notifyObservers(org.puremvc.python.patterns.observer.Notification(self.NOTE1))
		self.assertEqual(True, self.lastNotification != self.NOTE1)

		view.notifyObservers(org.puremvc.python.patterns.observer.Notification(self.NOTE2))
		self.assertEqual(True, self.lastNotification != self.NOTE2)

		self.__cleanup()									

	def testRemoveOneOfTwoMediatorsAndSubsequentNotify(self): 
		"""ViewTest: Test removing one of two Mediators and subsequent notify()"""
		
		view = org.puremvc.python.core.View.getInstance()
		
		view.registerMediator(utils.view.ViewTestMediator2(self))
	
		view.registerMediator(utils.view.ViewTestMediator3(self))
	
		view.notifyObservers(org.puremvc.python.patterns.observer.Notification(self.NOTE1))
		self.assertEqual(True, self.lastNotification == self.NOTE1)

		view.notifyObservers(org.puremvc.python.patterns.observer.Notification(self.NOTE2))
		self.assertEqual(True, self.lastNotification == self.NOTE2)

		view.notifyObservers(org.puremvc.python.patterns.observer.Notification(self.NOTE3))
		self.assertEqual(True, self.lastNotification == self.NOTE3)
			
		view.removeMediator(utils.view.ViewTestMediator2.NAME)
		
		self.assertEqual(True, view.retrieveMediator(utils.view.ViewTestMediator2.NAME) == None)

		self.lastNotification = None
	
		view.notifyObservers(org.puremvc.python.patterns.observer.Notification(self.NOTE1))
		self.assertEqual(True, self.lastNotification != self.NOTE1)

		view.notifyObservers(org.puremvc.python.patterns.observer.Notification(self.NOTE2))
		self.assertEqual(True, self.lastNotification != self.NOTE2)

		view.notifyObservers(org.puremvc.python.patterns.observer.Notification(self.NOTE3))
		self.assertEqual(True, self.lastNotification == self.NOTE3)
		
		self.__cleanup()									
