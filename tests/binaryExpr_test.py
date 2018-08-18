#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint

from lib.binaryExpr import BinaryExpr
from lib.numToken import NumToken
from lib.idToken import IdToken
from lib.astLeaf import ASTLeaf

class TestBinaryExpr(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.value1 = randint(1, 100)
        self.value2 = randint(1, 100)
        self.opText = '+'

        self.left = ASTLeaf(NumToken(self.lineNumber, self.value1))
        self.op = ASTLeaf(IdToken(self.lineNumber, self.opText))
        self.right = ASTLeaf(NumToken(self.lineNumber, self.value2))

        self.expr = BinaryExpr([self.left, self.op, self.right])

    def tearDown(self):
        pass

    def test_left(self):
        self.assertEqual(self.left, self.expr.left())

    def test_right(self):
        self.assertEqual(self.right, self.expr.right())

    def test_operator(self):
        self.assertEqual(self.op.token().getText(), self.expr.operator())

if __name__ == '__main__':
    unittest.main()
