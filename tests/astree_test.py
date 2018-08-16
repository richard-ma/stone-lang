#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from lib.astree import ASTree

class TestASTree(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_instance(self):
        # ASTree is an abstract class
        # if call ASTree.__init__() will raise a TypeError
        with self.assertRaises(TypeError):
            ASTree()

if __name__ == '__main__':
    unittest.main()
