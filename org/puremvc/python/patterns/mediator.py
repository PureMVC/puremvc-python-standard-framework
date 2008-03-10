import org.puremvc.python.interfaces
import org.puremvc.python.patterns.observer

class Mediator( org.puremvc.python.patterns.observer.Notifier, org.puremvc.python.interfaces.IMediator, org.puremvc.python.interfaces.INotifier ):
    """
    A base C{IMediator} implementation. 
    
    @see org.puremvc.core.view.View View
    """
    
    NAME = 'Mediator'
    
    __viewComponent = None
    
    def __init__( self, viewComponent = None ):
        """
        Constructor
        """
        self.__viewComponent
    
    def getMediatorName( self ):
        """
        Get the name of the C{Mediator}.

        Override in subclass!
        """
        return Mediator.NAME
    
    def getViewComponent( self ):
        """
        Get the C{Mediator}'s view component.

        Additionally, an implicit getter will usually
        be defined in the subclass that casts the view 
        object to a type.
        """
        return self.__viewComponent
    
    def listNotificationInterests( self ):
        """
        List the C{INotification} names this
        C{Mediator} is interested in being notified of.
        
        @return: Array the list of C{INotification} names 
        """
        return ()
    
    def handleNotification( self, notification ):
        """
        Handle C{INotification}s.
        
        Typically this will be handled in a switch statement,
        with one 'case' entry per C{INotification}
        the C{Mediator} is interested in.
        """
        pass