#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from src.astree import ASTree

class TestASTree(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.child1 = ASTree()
        self.child2 = ASTree()
        self.astree = ASTree()

    def tearDown(self):
        pass

    def append_childs(self):
        self.astree.add(self.child1)
        self.astree.add(self.child2)

    def test_append(self):
        self.astree.add(self.child1)
        self.assertEqual(self.astree.numChildren(), 1)

    def test_child(self):
        self.append_childs()
        self.assertEqual(self.astree.child(0), self.child1)
        self.assertEqual(self.astree.child(1), self.child2)

    def test_numChildren(self):
        self.append_childs()
        self.assertEqual(self.astree.numChildren(), 2)

    def test_location(self):
        self.assertIsNone(self.astree.location())

    def test_children(self):
        self.append_childs()
        self.assertListEqual(
                self.astree.children(),
                [self.child1, self.child2])

if __name__ == '__main__':
    unittest.main()
