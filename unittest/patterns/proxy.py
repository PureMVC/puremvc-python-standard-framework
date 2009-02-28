import unittest

import puremvc.patterns.proxy

class ProxyTest(unittest.TestCase):
    """ProxyTest: Test Proxy Pattern"""

    def testNameAccessor(self):
        """ProxyTest: Test Name Accessor"""

        prxy = puremvc.patterns.proxy.Proxy('TestProxy')
        self.assertEqual(True, prxy.getProxyName() == 'TestProxy')

    def testDataAccessors(self): 
        """ProxyTest: Test Data Accessors"""
        
        prxy = puremvc.patterns.proxy.Proxy('colors')
        prxy.setData(['red', 'green', 'blue'])
        data = prxy.getData()

        self.assertEqual(True, len(data) == 3)
        self.assertEqual(True, data[0]  == 'red')
        self.assertEqual(True, data[1]  == 'green')
        self.assertEqual(True, data[2]  == 'blue')

    def testConstructor(self): 
        """ProxyTest: Test Constructor"""

        prxy = puremvc.patterns.proxy.Proxy('colors',['red', 'green', 'blue'])
        data = prxy.getData()

        self.assertEqual(True, prxy is not None)
        self.assertEqual(True, prxy.getProxyName() == 'colors')
        self.assertEqual(True, len(data) == 3)
        self.assertEqual(True, data[0]  == 'red')
        self.assertEqual(True, data[1]  == 'green')
        self.assertEqual(True, data[2]  == 'blue')
