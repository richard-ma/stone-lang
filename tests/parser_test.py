#!/usr/bin/env python
# encoding: utf-8

import unittest

from lib.parser import *

class TestParser_Element(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        with self.assertRaises(TypeError):
            Parser.Element()

if __name__ == '__main__':
    unittest.main()
