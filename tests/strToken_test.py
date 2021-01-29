#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint

from lib.strToken import StrToken
from lib.stoneException import StoneException

class TestStrToken(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.string = str(randint(1, 100))
        self.token = StrToken(self.lineNumber, self.string)

    def tearDown(self):
        pass

    def test_isString(self):
        self.assertEqual(True, self.token.isString())

    def test_getText(self):
        self.assertEqual(self.string, self.token.getText())

    def test_getNumber(self):
        self.assertRaises(StoneException)

    def test_isIdentifier(self):
        self.assertEqual(False, self.token.isIdentifier())

    def test_isNumber(self):
        self.assertEqual(False, self.token.isNumber())



if __name__ == '__main__':
    unittest.main()
