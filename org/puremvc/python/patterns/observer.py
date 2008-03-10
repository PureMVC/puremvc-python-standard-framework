import org.puremvc.python.interfaces
import org.puremvc.python.patterns.command
from array import array

class Notification( org.puremvc.python.interfaces.INotification ):
    """
    A base C{INotification} implementation.
    
    The Observer Pattern as implemented within PureMVC exists 
    to support event-driven communication between the 
    application and the actors of the MVC triad.
    
    Generally, C{IMediator} implementors
    place event listeners on their view components, which they
    then handle in the usual way. This may lead to the broadcast of C{Notification}s to 
    trigger C{ICommand}s or to communicate with other C{IMediators}. C{IProxy} and C{ICommand}
    instances communicate with each other and C{IMediator}s 
    by broadcasting C{INotification}s.
    
    PureMVC C{Notification}s follow a 'Publish/Subscribe'
    pattern. PureMVC classes need not be related to each other in a 
    parent/child relationship in order to communicate with one another
    using C{Notification}s.
    
    @see org.puremvc.patterns.observer.Observer Observer
    """
    __name = None
    __body = None
    __type = None
    
    def __init__( self, name, body = None, type = None ):
        """
        Constructor. 
        
        @param name name of the C{Notification} instance. (required)
        @param body the C{Notification} body. (optional)
        @param type the type of the C{Notification} (optional)
        """
        self.__name = name
        self.__body = body
        self.__type = type
       
    def getName( self ):
        """
        Get the name of the C{Notification} instance.
        
        @return the name of the C{Notification} instance.
        """
        return self.__name
    
    def setBody( self, body ):
        """
        Set the body of the C{Notification} instance.
        """
        self.__body = body
    
    def getBody( self ):
        """
        Get the body of the C{Notification} instance.
        
        @return the body object. 
        """
        return self.__body
    
    def setBType( self, type ):
        """
        Set the type of the C{Notification} instance.
        """
        self.__type = type
    
    def getType( self ):
        """
        Get the type of the C{Notification} instance.
        
        @return the type  
        """
        return self.__type
    
    def __str__( self ):
        """
        Get the string representation of the C{Notification} instance.
        
        @return: the string representation of the C{Notification} instance.
        """
        msg = "Notification Name: " + self.getName()
        msg += "\nBody:" + self.__body
        msg += "\nType:" + self.__type
        return msg

class Notifier( org.puremvc.python.interfaces.INotifier ):
    """
    A Base C{INotifier} implementation.
    
    
    C{MacroCommand, Command, Mediator} and C{Proxy} 
    all have a need to send C{Notifications}. 
    
    The C{INotifier} interface provides a common method called
    C{sendNotification} that relieves implementation code of 
    the necessity to actually construct C{Notifications}.
    
    
    The C{Notifier} class, which all of the above mentioned classes
    extend, provides an initialized reference to the C{Facade}
    Singleton, which is required for the convienience method
    for sending C{Notifications}, but also eases implementation as these
    classes have frequent C{Facade} interactions and usually require
    access to the facade anyway.
    
    @see org.puremvc.patterns.facade.Facade Facade
    @see org.puremvc.patterns.mediator.Mediator Mediator
    @see org.puremvc.patterns.proxy.Proxy Proxy
    @see org.puremvc.patterns.command.SimpleCommand SimpleCommand
    @see org.puremvc.patterns.command.MacroCommand MacroCommand
    """
    __facade = org.puremvc.python.patterns.facade.Facade.getInstance()
    
    def sendNotification( self, notificationName, body = None, type = None ):
        """
        Send an C{INotification}s.
        
        Keeps us from having to construct new notification 
        instances in our implementation code.
        @param notificationName the name of the notiification to send
        @param body the body of the notification (optional)
        @param type the type of the notification (optional)
        """
        self.__facade.notifyObservers( org.puremvc.python.patterns.observer.Notification( notificationName, body, type ) )

class Observer( org.puremvc.python.interfaces.IObserver ):
    """
    A base C{IObserver} implementation.
     
    An C{Observer} is an object that encapsulates information
    about an interested object with a method that should 
    be called when a particular C{INotification} is broadcast. 
    
    In PureMVC, the C{Observer} class assumes these responsibilities:
    - Encapsulate the notification (callback) method of the interested object.
    - Encapsulate the notification context (this) of the interested object.
    - Provide methods for setting the notification method and context.
    - Provide a method for notifying the interested object.
    
    
    @see org.puremvc.core.view.View View
    @see org.puremvc.patterns.observer.Notification Notification
    """
    notify = None
    context = None
    
    def __init__( self, notifyMethod, notifyContext ):
        """
        Constructor. 
        
        The notification method on the interested object should take 
        one parameter of type C{INotification}
        
        @param notifyMethod: the notification method of the interested object
        @param notifyContext: the notification context of the interested object
        """
        self.setNotifyMethod( notifyMethod )
        self.setNotifyContext( notifyContext )
    
    def setNotifyMethod( self, notifyMethod ):
        """
        Set the notification method.
        
        The notification method should take one parameter of type C{INotification}.
        
        @param notifyMethod: the notification (callback) method of the interested object.
        """
        self.notify = notifyMethod
    
    def setNotifyContext( self, notifyContext ):
        """
        Set the notification context.
        
        @param notifyContext: the notification context (this) of the interested object.
        """
        self.context = notifyContext
        
    def getNotifyMethod( self ):
        """
        Get the notification method.
        
        @return: the notification (callback) method of the interested object.
        """
        return self.notify
    
    def getNotifyContext( self ):
        """
        Get the notification context.
        
        @return: the notification context (C{this}) of the interested object.
        """
        return self.context
    
    def notifyObserver( self, notification ):
        """
        Notify the interested object.
        
        @param notification: the C{INotification} to pass to the interested object's notification method.
        """
        eval( self.getNotifyMethod() )( self.getNotifyContext(), array( notification ) )
    
    def compareNotifyContext( self, object ):
        """
        Compare an object to the notification context. 
        
        @param object: the object to compare
        @return boolean: indicating if the object and the notification context are the same
        """
        return object is self.context