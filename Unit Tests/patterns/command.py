import unittest

import puremvc.patterns.observer
import utils.command

class CommandTest(unittest.TestCase):
    """CommandTest: Test Command Pattern"""
    
    def testMacroCommandExecute(self):
        """CommandTest: Test MacroCommand execute()"""
        
        vo = utils.command.MacroCommandTestVO(5)
        note = puremvc.patterns.observer.Notification('MacroCommandTest', vo)    
        command = utils.command.MacroCommandTestCommand()
        command.execute(note);
        
        self.assertEqual(True, vo.result1 == 10)
        self.assertEqual(True, vo.result2 == 25)

    def testSimpleCommandExecute(self):
        """CommandTest: Test SimpleCommand execute()"""

        vo = utils.command.SimpleCommandTestVO(5)
        note = puremvc.patterns.observer.Notification('SimpleCommandTestNote', vo)
        command = utils.command.SimpleCommandTestCommand()
        command.execute(note);

        self.assertEqual(True, vo.result == 10)
