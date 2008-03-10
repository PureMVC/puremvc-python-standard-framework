import org.puremvc.python.core.view
import org.puremvc.python.core.model
import org.puremvc.python.core.controller
import org.puremvc.python.interfaces

class Facade( org.puremvc.python.interfaces.IFacade ):
    """
    A base Singleton C{IFacade} implementation.
    
    
    In PureMVC, the C{Facade} class assumes these 
    responsibilities:
    
    - Initializing the C{Model}, C{View}
    and C{Controller} Singletons. 
    - Providing all the methods defined by the C{IModel, 
    IView, & IController} interfaces.
    - Providing the ability to override the specific C{Model},
    C{View} and C{Controller} Singletons created. 
    - Providing a single point of contact to the application for 
    registering C{Commands} and notifying C{Observers}
    
    
    Example usage:
    C{
    from org.puremvc.patterns.facade import Facade;
    
    from com.me.myapp.model import *;
    from com.me.myapp.view import *;
    from com.me.myapp.controller import *;

    class MyFacade( Facade )
        # Notification constants. The Facade is the ideal
        # location for these constants, since any part
        # of the application participating in PureMVC 
        # Observer Notification will know the Facade.
        GO_COMMAND = "go"
            
        # Override Singleton Factory method 
        @staticmethod
        def getInstance():
            if __facade__instance == null:
                __facade__instance = MyFacade()
            return (MyFacade)__facade__instance
            
        # optional initialization hook for Facade
        def initializeFacade( self ):
            super.initializeFacade()
            # do any special subclass initialization here
       
        # optional initialization hook for Controller
        def initializeController( self ):
            # call super to use the PureMVC Controller Singleton. 
            super.initializeController()
    
            # Otherwise, if you're implmenting your own
            # IController, then instead do:
            # if not controller == null:
            #     return
            # controller = MyAppController.getInstance()
            
            # do any special subclass initialization here
            # such as registering Commands
            registerCommand( GO_COMMAND, com.me.myapp.controller.GoCommand )
       
        # optional initialization hook for Model
        def initializeModel( self ):
            # call super to use the PureMVC Model Singleton. 
            super.initializeModel()
    
            # Otherwise, if you're implmenting your own
            # IModel, then instead do:
            # if not model == null:
            #     return;
            # __facade__model = MyAppModel.getInstance()
            
            # do any special subclass initialization here
            # such as creating and registering Model proxys
            # that don't require a facade reference at
            # construction time, such as fixed type lists
            # that never need to send Notifications.
            regsiterProxy( new USStateNamesProxy() )
                
            # CAREFUL: Can't reference Facade instance in constructor 
            # of new Proxys from here, since this step is part of
            # Facade construction!  Usually, Proxys needing to send 
            # notifications are registered elsewhere in the app 
            # for this reason.
       
            # optional initialization hook for View
            def initializeView( self ):
                # call super to use the PureMVC View Singleton. 
                super.initializeView();
    
                # Otherwise, if you're implmenting your own
                # IView, then instead do:
                # if not view == null:
                #     return
                # __facade__view = MyAppView.getInstance()
            
                # do any special subclass initialization here
                # such as creating and registering Mediators
                # that do not need a Facade reference at construction
                # time.
                registerMediator( LoginMediator() )
    
                # CAREFUL: Can't reference Facade instance in constructor 
                # of new Mediators from here, since this is a step
                # in Facade construction! Usually, all Mediators need 
                # receive notifications, and are registered elsewhere in 
                # the app for this reason.
    
    @see org.puremvc.core.model.Model Model
    @see org.puremvc.core.view.View View
    @see org.puremvc.core.controller.Controller Controller
    @see org.puremvc.patterns.observer.Notification Notification
    @see org.puremvc.patterns.mediator.Mediator Mediator
    @see org.puremvc.patterns.proxy.Proxy Proxy
    @see org.puremvc.patterns.command.SimpleCommand SimpleCommand
    @see org.puremvc.patterns.command.MacroCommand MacroCommand
    """
    __controller = None
    __model = None
    __view = None
    __instance = None
    
    def __init__( self ):
        """
        Constructor. 
        
        
        This C{IFacade} implementation is a Singleton, 
        so you should not call the constructor 
        directly, but instead call the static Singleton 
        Factory method C{Facade.getInstance()}
        
        @throws Error Error if Singleton instance has already been constructed
        """
        if self.__instance != None:
            raise Exception
        self.initializeFacade()
        
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
    
    def initializeFacade( self ):
        """
        Initialize the Singleton C{Facade} instance.
        
        Called automatically by the constructor. Override in your
        subclass to do any subclass specific initializations. Be
        sure to call C{super.initializeFacade()}, though.
        """
        self.initializeModel()
        self.initializeController()
        self.initializeView()
    
    @staticmethod
    def getInstance():
        """
        Facade Singleton Factory method
        
        @return the Singleton instance of the Facade
        """
        if Facade.__instance == None:
            Facade.__instance = Facade()
            
        return Facade.__instance
    
    def initializeController( self ):
        """
        Initialize the C{Controller}.
        
        Called by the C{initializeFacade} method.
        Override this method in your subclass of C{Facade} 
        if one or both of the following are true:
        - You wish to initialize a different C{IController}.
        - You have C{Commands} to register with the C{Controller} at startup.}.           
        
        If you don't want to initialize a different C{IController}, 
        call C{super.initializeController()} at the beginning of your
        method, then register C{Command}s.
        """
        if not self.__controller == None:
            return
        self.__controller = org.puremvc.python.core.controller.Controller.getInstance()
        
    def initializeView( self ):
        """
        Initialize the C{Model}.
        
        
        Called by the C{initializeFacade} method.
        Override this method in your subclass of C{Facade} 
        if one or both of the following are true:
        
        - You wish to initialize a different C{IModel}.
        - You have C{Proxy}s to register with the Model that do not 
        retrieve a reference to the Facade at construction time.} 
        
        If you don't want to initialize a different C{IModel}, 
        call C{super.initializeModel()} at the beginning of your
        method, then register C{Proxy}s.
        
        Note: This method is I{rarely} overridden; in practice you are more
        likely to use a C{Command} to create and register C{Proxy}s
        with the C{Model}, since C{Proxy}s with mutable data will likely
        need to send C{INotification}s and thus will likely want to fetch a reference to 
        the C{Facade} during their construction. 
        """
        if not self.__view == None:
            return
        self.__view = org.puremvc.python.core.view.View.getInstance()
    
    def initializeModel( self ):
        """
        Initialize the C{View}.
        
        
        Called by the C{initializeFacade} method.
        Override this method in your subclass of C{Facade} 
        if one or both of the following are true:
        
        - You wish to initialize a different C{IView}.
        - You have C{Observers} to register with the C{View}
        
        If you don't want to initialize a different C{IView}, 
        call C{super.initializeView()} at the beginning of your
        method, then register C{IMediator} instances.
        
        Note: This method is I{rarely} overridden; in practice you are more
        likely to use a C{Command} to create and register C{Mediator}s
        with the C{View}, since C{IMediator} instances will need to send 
        C{INotification}s and thus will likely want to fetch a reference 
        to the C{Facade} during their construction. 
        """
        if not self.__model == None:
            return
        self.__model = org.puremvc.python.core.model.Model.getInstance()
    
    def notifyObservers( self, notification ):
        """
        Notify C{Observer}s.
        
        @param notification the C{INotification} to have the C{View} notify C{Observers} of.
        """
        if not self.__view == None:
            self.__view.notifyObservers( notification )
    
    def registerCommand( self, notificationName, commandClassRef ):
        """
        Register an C{ICommand} with the C{Controller} by Notification name.
        
        @param notificationName the name of the C{INotification} to associate the C{ICommand} with
        @param commandClassRef a reference to the Class of the C{ICommand}
        """
        self.__controller.registerCommand( notificationName, commandClassRef )
    
    def removeCommand( self, notificationName ):
        """
        Remove a previously registered C{ICommand} to C{INotification} mapping from the Controller.
        
        @param notificationName the name of the C{INotification} to remove the C{ICommand} mapping for
        """
        self.__controller.removeCommand( notificationName )
        
    def registerProxy( self, proxy ):
        """
        Register an C{IProxy} with the C{Model} by name.
        
        @param proxyName the name of the C{IProxy}.
        @param proxy the C{IProxy} instance to be registered with the C{Model}.
        """
        self.__model.registerProxy( proxy )
    
    def retrieveProxy( self, proxyName ):
        """
        Retrieve an C{IProxy} from the C{Model} by name.
        
        @param proxyName the name of the proxy to be retrieved.
        @return the C{IProxy} instance previously registered with the given C{proxyName}.
        """
        return self.__model.retrieveProxy( proxyName )
    
    def removeProxy( self, proxyName ):
        """
        Remove an C{IProxy} from the C{Model} by name.
         *
        @param proxyName the C{IProxy} to remove from the C{Model}.
        """
        if not self.__model == None:
            self.__model.removeProxy( proxyName )
    
    def registerMediator( self, mediator ):
        """
        Register a C{IMediator} with the C{View}.
        
        @param mediatorName the name to associate with this C{IMediator}
        @param mediator a reference to the C{IMediator}
        """
        if not self.__view == None:
            self.__view.registerMediator( mediator )
    
    def retrieveMediator( self, mediatorName ):
        """
        Retrieve an C{IMediator} from the C{View}.
        
        @param mediatorName
        @return the C{IMediator} previously registered with the given C{mediatorName}.
         */
        """
        return self.__view.retrieveMediator( mediatorName )
    
    def removeMediator( self, mediatorName ):
        """
        Remove an C{IMediator} from the C{View}.
        
        @param mediatorName name of the C{IMediator} to be removed.
        """
        if not self.__view == None:
            self.__view.removeMediator( mediatorName )
    