#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from src.astree import ASTree

class TestASTree(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.astree = ASTree()

    def tearDown(self):
        pass

    def test_append(self):
        child = ASTree()
        self.astree.add(child)
        assert self.astree.numChildren() == 1
        assert self.astree.child(0) == child

    def test_child(self):
        pass

if __name__ == '__main__':
    unittest.main()
