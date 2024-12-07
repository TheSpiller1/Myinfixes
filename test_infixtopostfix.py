
import unittest
from infixtopostfix import swap


class TestInfixToPostfix(unittest.TestCase):

    def test_postfix(self):
        self.assertEqual(swap("a+b*c+d"), "abc*+d+")
        self.assertEqual(swap("(a+b)*(c+d)"), "ab+cd+*")
        self.assertEqual(swap("(a+(b+c))*(c/b)"), "abc++cb/*")


