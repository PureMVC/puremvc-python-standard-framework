import org.puremvc.python.patterns.observer
import org.puremvc.python.interfaces
import org.puremvc.python.patterns.mediator

class ViewTestNote(org.puremvc.python.patterns.observer.Notification, org.puremvc.python.interfaces.INotification):

	NAME = "ViewTestNote"
	
	def __init__(self, anme, body):
		org.puremvc.python.patterns.observer.Notification.__init__(self, ViewTestNote.NAME, body)
		
	@staticmethod
	def create(body):		
		return ViewTestNote(ViewTestNote.NAME, body)	

class ViewTestMediator(org.puremvc.python.patterns.mediator.Mediator, org.puremvc.python.interfaces.IMediator):

	NAME = 'ViewTestMediator'
		
	def __init__(self, view):
		org.puremvc.python.patterns.mediator.Mediator.__init__(self, ViewTestMediator.NAME, view)

	def listNotificationInterests(self):
		return ['ABC', 'DEF', 'GHI']

class ViewTestMediator2(org.puremvc.python.patterns.mediator.Mediator, org.puremvc.python.interfaces.IMediator):

	NAME = 'ViewTestMediator2'

	def __init__(self, view):
		org.puremvc.python.patterns.mediator.Mediator.__init__(self, ViewTestMediator2.NAME, view)

	def listNotificationInterests(self):
		return [self.viewComponent.NOTE1,  self.viewComponent.NOTE2]

	def handleNotification(self, notification):
		self.viewComponent.lastNotification = notification.getName()
				
class ViewTestMediator3(org.puremvc.python.patterns.mediator.Mediator, org.puremvc.python.interfaces.IMediator):

	NAME = 'ViewTestMediator3'

	def __init__(self, view):
		org.puremvc.python.patterns.mediator.Mediator.__init__(self, ViewTestMediator3.NAME, view)

	def listNotificationInterests(self):
		return [self.viewComponent.NOTE3]

	def handleNotification(self, notification):
		self.viewComponent.lastNotification = notification.getName()
		
class ViewTestMediator4(org.puremvc.python.patterns.mediator.Mediator, org.puremvc.python.interfaces.IMediator):

	NAME = 'ViewTestMediator4'

	def __init__(self, view):
		org.puremvc.python.patterns.mediator.Mediator.__init__(self, ViewTestMediator4.NAME, view)

	def onRegister(self):
		self.viewComponent.onRegisterCalled = True

	def onRemove(self):
		self.viewComponent.onRemoveCalled = True