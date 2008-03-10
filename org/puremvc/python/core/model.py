"""

PureMVC Python Port by Nathan Levesque <nathan.levesque@puremvc.org> 

PureMVC - Copyright(c) 2006, 2007 Futurescale, Inc., Some rights reserved. 

Your reuse is governed by the Creative Commons Attribution 3.0 License 

"""

import org.puremvc.python.interfaces

class Model( org.puremvc.python.interfaces.IModel ):
    """
    A Singleton C{IModel} implementation.

    In PureMVC, the C{Model} class provides
    access to model objects (Proxies) by named lookup.

    The C{Model} assumes these responsibilities:

    - Maintain a cache of C{IProxy} instances.
    - Provide methods for registering, retrieving, and removing 
    C{IProxy} instances.

    Your application must register C{IProxy} instances 
    with the C{Model}. Typically, you use an 
    C{ICommand} to create and register C{IProxy} 
    instances once the C{Facade} has initialized the Core 
    actors.

    @see org.puremvc.patterns.proxy.Proxy Proxy
    @see org.puremvc.interfaces.IProxy IProxy

    """
    __proxyMap = None
    __instance = None
    
    def __init__( self ):
        """
        Constructor. 

        This C{IModel} implementation is a Singleton, 
        so you should not call the constructor 
        directly, but instead call the static Singleton 
        Factory method C{Model.getInstance()}
         
        @raise Exception: Exception if Singleton instance has already been constructed
        """
        if self.__instance != None:
            raise Exception
        self.__proxyMap = ()
        self.initializeModel()
    
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
    
    def initializeModel( self ):
        """
        Initialize the Singleton C{Model} instance.
        
        Called automatically by the constructor, this
        is your opportunity to initialize the Singleton
        instance in your subclass without overriding the
        constructor.
        
        @return void
        """
        pass
    
    @staticmethod
    def getInstance( self ):
        """
        C{Model} Singleton Factory method.
        
        @return the Singleton instance
        """
        if Model.__instance == None:
            Model.__instance = Model()
            
        return Model.__instance
    
    def registerProxy( self, proxy ):
        """
        Register an C{IProxy} with the C{Model}.
        
        @param proxy an C{IProxy} to be held by the C{Model}.
        """
        self.__proxyMap[ proxy.getProxyName() ] = proxy
    
    def retrieveProxy( self, proxyName ):
        """
        Retrieve an C{IProxy} from the C{Model}.
        
        @param proxyName: name of the C{IProxy} instance to retrieve.
        """
        return self.__proxyMap[ proxyName ]
    
    def removeProxy( self, proxyName ):
        """
        Remove an C{IProxy} from the C{Model}.

        @param proxyName: name of the C{IProxy} instance to be removed.
        """
        self.__proxyMap[ proxyName ] = None