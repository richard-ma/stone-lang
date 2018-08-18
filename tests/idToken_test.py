#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint

from lib.idToken import IdToken

class TestIdToken(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.text = str(randint(1, 100))
        self.token = IdToken(self.lineNumber, self.text)

    def tearDown(self):
        pass

    def test_isIdentifier(self):
        self.assertEqual(True, self.token.isIdentifier())

    def test_getText(self):
        self.assertEqual(self.text, self.token.getText())

    def test_isNumber(self):
        self.assertEqual(False, self.token.isNumber())

    def test_isString(self):
        self.assertEqual(False, self.token.isString())

if __name__ == '__main__':
    unittest.main()
