import org.puremvc.python.interfaces
import org.puremvc.python.patterns.observer

class Proxy( org.puremvc.python.patterns.observer.Notifier, org.puremvc.python.interfaces.IProxy, org.puremvc.python.interfaces.INotifier ):
    """
    A base C{IProxy} implementation. 
    
    In PureMVC, C{Proxy} classes are used to manage parts of the 
    application's data model.

    A C{Proxy} might simply manage a reference to a local data object, 
    in which case interacting with it might involve setting and 
    getting of its data in synchronous fashion.

    C{Proxy} classes are also used to encapsulate the application's 
    interaction with remote services to save or retrieve data, in which case, 
    we adopt an asyncronous idiom; setting data (or calling a method) on the 
    C{Proxy} and listening for a C{Notification} to be sent 
    when the C{Proxy} has retrieved the data from the service.
    
    @see org.puremvc.core.model.Model Model
    """
    NAME = 'Proxy'
    __proxyName = None
    __data = None
    
    def __init__( self, proxyName = None, data = None ):
        """
        Constructor
        """
        self.__proxyName = (proxyName != None) and proxyName or Proxy.NAME
        if data != None:
            self.setData( data )
    
    def getProxyName( self ):
        """
        Get the proxy name
        """
        return self.__proxyName
    
    def setData( self, data ):
        """
        Set the  data object
        """
        self.__data = data
    
    def getData( self ):
        """
        Get the data object
        """
        return self.__data