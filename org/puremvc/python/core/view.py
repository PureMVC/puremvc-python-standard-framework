"""

PureMVC Python Port by Nathan Levesque <nathan.levesque@puremvc.org> 

PureMVC - Copyright(c) 2006, 2007 Futurescale, Inc., Some rights reserved. 

Your reuse is governed by the Creative Commons Attribution 3.0 License 

"""

import org.puremvc.python.interfaces
import org.puremvc.python.patterns.observer

class View( org.puremvc.python.interfaces.IView ):
    """
    A Singleton C{IView} implementation.
    
    In PureMVC, the C{View} class assumes these responsibilities:
    - Maintain a cache of C{IMediator} instances.
    - Provide methods for registering, retrieving, and removing C{IMediators}.
    - Managing the observer lists for each C{INotification} in the application.
    - Providing a method for attaching C{IObservers} to an C{INotification}'s observer list.
    - Providing a method for broadcasting an C{INotification}.
    
    @see org.puremvc.patterns.mediator.Mediator Mediator
    @see org.puremvc.patterns.observer.Observer Observer
    @see org.puremvc.patterns.observer.Notification Notification
    """
    __mediatorMap = None
    __observerMap = None
    __instance = None
    
    def __init__( self ):
        """
        Constructor. 
        
        This C{IView} implementation is a Singleton, 
        so you should not call the constructor 
        directly, but instead call the static Singleton 
        Factory method C{View.getInstance()}
        
        @raise Exception: Exception if Singleton instance has already been constructed
        """
        if self.__instance != None:
            raise Exception
        self.__observerMap = ()
        self.__mediatorMap = ()
        self.initializeView()
    
    def __new__( cls ):
        """
        Enforces the Singleton Pattern which this class. This is a 
        Python-specific implementation. This function should 
        never be called directly.
        
        @param: The class to be instaniated and assigned 
        to the __instance variable.
        """
        if not '__instance' in type.__dict__:
            type.__instance = object.__new__(type)
        return type.__instance
    
    def initializeView( self ):
        """
        Initialize the Singleton View instance.

        Called automatically by the constructor, this
        is your opportunity to initialize the Singleton
        instance in your subclass without overriding the
        constructor.

        @return void
        """
        pass
    
    @staticmethod
    def getInstance():
        """
        View Singleton Factory method.
        
        @return the Singleton instance of C{View}
        """
        if View.__instance == None:
            View.__instanc = View()
            
        return View.__instance
    
    def registerObserver( self, notificationName, observer ):
        """
        Register an C{IObserver} to be notified
        of C{INotifications} with a given name.
         
        @param notificationName: the name of the C{INotifications} to notify this C{IObserver} of
        @param observer: the C{IObserver} to register
        
        """
        if not self.__observerMap[ notificationName ] == None:
            self.__observerMap[ notificationName ].append( observer )
        else:
            self.__observerMap[ notificationName ] = observer
    
    def notifyObservers( self, notification ):
        """
        Notify the C{IObservers} for a particular C{INotification}.

        All previously attached C{IObservers} for this C{INotification}'s
        list are notified and are passed a reference to the C{INotification} in 
        the order in which they were registered.</P>

        @param notification: the C{INotification} to notify C{IObservers} of.
        """
        if not self.__observerMap[ notification.getName() ] == None:
            observers = self.__oobserverMap[ notification.getName() ]
            for i in range( len( observers ) ):
                observer = observers[ i ]
                observer.notifyObserver( notification )
    
    def registerMediator( self, mediator ):
        """
        Register an C{IMediator} instance with the C{View}.
        
        Registers the C{IMediator} so that it can be retrieved by name,
        and further interrogates the C{IMediator} for its 
        C{INotification} interests.

        If the C{IMediator} returns any C{INotification} 
        names to be notified about, an C{Observer} is created encapsulating 
        the C{IMediator} instance's C{handleNotification} method 
        and registering it as an C{Observer} for all C{INotifications} the 
        C{IMediator} is interested in.

        @param mediatorName: the name to associate with this C{IMediator} instance
        @param mediator: a reference to the C{IMediator} instance
        """
        self.__mediatorMap[ mediator.getMediatorName() ] = mediator
        
        interests = mediator.listNotificationInterests()
        if len( interests ) == 0:
            return
        
        observer = org.puremvc.python.patterns.observer.Observer( mediator.handleNotification, mediator )
        
        for i in range( len( interests ) ):
            self.registerObserver( interests[ i ], observer )
    
    def retrieveMediator( self, mediatorName ):
        """
        Retrieve an C{IMediator} from the C{View}.
        
        @param mediatorName: the name of the C{IMediator} instance to retrieve.
        @return the C{IMediator} instance previously registered with the given C{mediatorName}.
        """
        return self.__mediatorMap[ mediatorName ]
    
    def removeMediator( self, mediatorName ):
        """
        Remove an C{IMediator} from the C{View}.
        
        @param mediatorName: name of the C{IMediator} instance to be removed.
        """
        for notificationName in self.__observerMap:
            observers = self.__observerMap[ notificationName ]
            
            removalTargets = ()
            for i in range( len( observers ) ):
                if org.puremvc.python.patterns.observer.Observer( observers[ i ] ).compareNotifyContext( self.removeMediator( mediatorName ) ) == True:
                    removalTargets.append( i )
                    
            target = None
            
            while len( removalTargets ) > 0:
                target = removalTargets.pop()
                observers.pop( target )
            
            if len( observers ) == 0:
                self.__observerMap.remove( mediatorName )
                break
        
        self.__mediatorMap.remove( mediatorName )
