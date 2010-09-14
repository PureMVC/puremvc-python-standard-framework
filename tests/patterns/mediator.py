import unittest

import puremvc.patterns.mediator as mediator

class MediatorTest(unittest.TestCase):
    """MediatorTest: Test Mediator Pattern"""

    def testNameAccessor(self):
        """MediatorTest: Test getMediatorName()"""    
        mdiatr = mediator.Mediator();
        self.assertEqual(True, mdiatr.getMediatorName() == mediator.Mediator.NAME );

    def testViewAccessor(self):
        """MediatorTest: Test getViewComponent()"""

        view = object()
        mdiatr = mediator.Mediator(mediator.Mediator.NAME, view);
        self.assertEqual(True, mdiatr.getViewComponent() is not None)
