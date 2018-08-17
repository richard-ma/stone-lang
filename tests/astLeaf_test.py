#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint

from lib.astLeaf import ASTLeaf
from lib.numToken import NumToken

class TestASTLeaf(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.value = randint(1, 100)
        self.token = NumToken(self.lineNumber, self.value)
        self.astLeaf = ASTLeaf(self.token)

    def tearDown(self):
        pass

    def test_child(self):
        with self.assertRaises(NotImplementedError):
            self.astLeaf.child(0)

    def test_numChildren(self):
        with self.assertRaises(NotImplementedError):
            self.astLeaf.numChildren()

    def test_location(self):
        self.assertEqual(self.astLeaf.location(), "at line %d" % (self.lineNumber))

    def test_token(self):
        self.assertEqual(self.astLeaf.token(), self.token)

    def test_add(self):
        with self.assertRaises(NotImplementedError):
            self.astLeaf.add('fakeToken')
