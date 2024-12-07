import unittest
from postfixtoprefix import change, inputer


class TestInfixToPostfix(unittest.TestCase):

    def test_postfix(self):
        self.assertEqual(change("abc*+d+"), "++a*bcd")
        self.assertEqual(change("ab+cd+*"), "*+ab+cd")
        self.assertEqual(change("abc++cb/*"), "*+a+bc/cb")

    def test_input(self):
        self.assertEqual(inputer(), "abc*+d+")
        self.assertEqual(inputer(), "ab+cd+*")
        self.assertEqual(inputer(), "abc++cb/*")


if __name__ == '__main__':
    unittest.main()