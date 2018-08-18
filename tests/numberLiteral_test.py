#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint

from lib.numberLiteral import NumberLiteral
from lib.numToken import NumToken

class TestNumberLiteral(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.value = randint(1, 100)
        self.token = NumToken(self.lineNumber, self.value)
        self.nl = NumberLiteral(self.token)

    def tearDown(self):
        pass

    def test_value(self):
        self.assertEqual(self.value, self.nl.value())


if __name__ == '__main__':
    unittest.main()
