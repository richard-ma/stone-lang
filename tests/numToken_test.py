#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint

from lib.numToken import NumToken

class TestNumToken(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.value = randint(1, 100)
        self.token = NumToken(self.lineNumber, self.value)

    def tearDown(self):
        pass

    def test_isNumber(self):
        self.assertEqual(self.token.isNumber(), True)

    def test_getText(self):
        self.assertEqual(self.token.getText(), str(self.value))

    def test_getNumber(self):
        self.assertEqual(self.token.getNumber(), self.value)


