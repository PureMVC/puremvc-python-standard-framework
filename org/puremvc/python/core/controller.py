"""

PureMVC Python Port by Nathan Levesque <nathan.levesque@puremvc.org> 

PureMVC - Copyright(c) 2006, 2007 Futurescale, Inc., Some rights reserved. 

Your reuse is governed by the Creative Commons Attribution 3.0 License 

"""

import org.puremvc.python.core.view
import org.puremvc.python.interfaces
import org.puremvc.python.patterns.observer

class Controller( org.puremvc.python.interfaces.IController ):
    """
    A Singleton C{IController} implementation. 
    
    In PureMVC, the C{Controller} class follows the
    'Command and Controller' strategy, and assumes these 
    responsibilities:
    
    - Remembering which C{ICommand}s 
    are intended to handle which C{INotifications}.
    - Registering itself as an C{IObserver} with
    the C{View} for each C{INotification} 
    that it has an C{ICommand} mapping for.
    - Creating a new instance of the proper C{ICommand}
    to handle a given C{INotification} when notified by the C{View}.
    - Calling the C{ICommand}'s C{execute}
    method, passing in the C{INotification}. 
    
    Your application must register C{ICommands} with the 
    Controller.
    
    The simplest way is to subclass C{Facade}, 
    and use its C{initializeController} method to add your 
    registrations. 
    
    @see org.puremvc.core.view.View View
    @see org.puremvc.patterns.observer.Observer Observer
    @see org.puremvc.patterns.observer.Notification Notification
    @see org.puremvc.patterns.command.SimpleCommand SimpleCommand
    @see org.puremvc.patterns.command.MacroCommand MacroCommand
    """
    __commandMap = None
    __view = None
    __instance = None

    def __init__( self ):
        """
        Constructor. 

        This C{IController} implementation is a Singleton, 
        so you should not call the constructor 
        directly, but instead call the static Singleton 
        Factory method C{Controller.getInstance()}
        
        @raise Exception: Exception if Singleton instance has already been constructed
        """
        
        if self.__instance != None:
            raise Exception
        self.__commandMap = ()
        self.initializeController()
        
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
    
    def initiailizeController( self ):
        """
        Initialize the Singleton C{Controller} instance.
        
        Called automatically by the constructor.
        
        Note that if you are using a subclass of C{View}
        in your application, you should <i>also</i> subclass C{Controller}
        and override the C{initializeController} method in the 
        following way:
        
        C{
               // ensure that the Controller is talking to my IView implementation
               def initializeController( self ):
                   __controller__view = MyView.getInstance()
        }
        
        This is due to Python's name mangling, which appends '__classname' to the
        front of variables declared with a name starting in a double underscore.
        This was used here to ensure no outside access to the __view variable.
        
        @return void
        """
        self.__view = org.puremvc.python.core.view.View.getInstance()
    
    @staticmethod
    def getInstance( self ):
        """
        C{Controller} Singleton Factory method.
        
        @return the Singleton instance of C{Controller}
        """
        if Controller.__instance == None:
            Controller.__instance = Controller()
            
        return Controller.__instance
    
    def executeCommand( self, note ):
        """
        If an C{ICommand} has previously been registered 
        to handle a the given C{INotification}, then it is executed.
        
        @param note an C{INotification}
        """
        commandClassRef = self.__commandMap[ note.getName() ]
        if commandClassRef == None:
            return
        
        commandInstance = eval( commandClassRef )()
        commandInstance.execute()
    
    def registerCommand( self, notificationName, commandClassRef ):
        """
        Register a particular C{ICommand} class as the handler 
        for a particular C{INotification}.
  
        If an C{ICommand} has already been registered to 
        handle C{INotification}s with this name, it is no longer
        used, the new C{ICommand} is used instead.
        
        The Observer for the new ICommand is only created if this the 
        first time an ICommand has been regisered for this Notification name.
        
        @param notificationName: the name of the C{INotification}
        @param commandClassRef: the C{Class} of the C{ICommand}
        """
        if self.__commandMap[ notificationName ] == None:
            self.__view.registerObserver( notificationName, org.puremvc.python.patterns.observer.Observer( self.executeCommand, self ) )
        
        self.__commandMap[ notificationName ] = commandClassRef
    
    def removeCommand( self, notificationName ):
        """
        Remove a previously registered C{ICommand} to C{INotification} mapping.
        
        @param notificationName: the name of the C{INotification} to remove the C{ICommand} mapping for  
        """
        self.__commandMap[ notificationName ] = None