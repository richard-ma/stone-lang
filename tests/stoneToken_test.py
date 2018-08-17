#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint

from lib.stoneToken import StoneToken

class TestStoneToken(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.token = StoneToken(self.lineNumber)

    def tearDown(self):
        pass

    def test_getLineNumber(self):
        self.assertEqual(self.token.getLineNumber(), self.lineNumber)

    def test_isIdentifier(self):
        self.assertEqual(self.token.isIdentifier(), False)

    def test_isNumber(self):
        self.assertEqual(self.token.isNumber(), False)

    def test_isString(self):
        self.assertEqual(self.token.isString(), False)

    def test_getText(self):
        self.assertEqual(self.token.getText(), "")

