#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint

from lib.astree import ASTree
from lib.astLeaf import ASTLeaf
from lib.astList import ASTList
from lib.numToken import NumToken

class TestASTList(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber1 = randint(1, 10)
        self.lineNumber2 = randint(1, 10)
        self.lineNumber3 = randint(1, 10)

        self.value1 = randint(1, 100)
        self.value2 = randint(1, 100)
        self.value3 = randint(1, 100)

        self.nt1 = NumToken(self.lineNumber1, self.value1)
        self.nt2 = NumToken(self.lineNumber2, self.value2)
        self.nt3 = NumToken(self.lineNumber3, self.value3)

        self.leaf1 = ASTLeaf(self.nt1)
        self.leaf2 = ASTLeaf(self.nt2)
        self.leaf3 = ASTLeaf(self.nt3)

        self.astList = ASTList([self.leaf1, self.leaf2, self.leaf3])

    def tearDown(self):
        pass

    def test_child(self):
        self.assertEqual(self.astList.child(0), self.leaf1)

    def test_numChildren(self):
        self.assertEqual(self.astList.numChildren(), 3)

    def test_children(self):
        self.assertListEqual(self.astList.children(),
                [self.leaf1, self.leaf2, self.leaf3])

    def test_str(self):
        self.assertEqual(str(self.astList),
                "(%d %d %d)" % (self.value1, self.value2, self.value3))

    def test_location(self):
        self.assertEqual(self.astList.location(),
                "at line %d" % (self.lineNumber1))

    def test_add(self):
        self.assertEqual(True, self.astList.add(self.leaf1))
        self.assertEqual(4, self.astList.numChildren())
        self.assertEqual(self.leaf1, self.astList.child(3))

        with self.assertRaises(TypeError) as e:
            self.astList.add('fake node')

        self.assertEqual("node is NOT ASTree type.",
                str(e.exception))


if __name__ == '__main__':
    unittest.main()
