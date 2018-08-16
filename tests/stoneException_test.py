#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from lib.stoneException import StoneException

class TestStoneException(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_StoneException(self):
        with self.assertRaises(StoneException) as e:
            raise StoneException("Error Message")

        self.assertEqual("Error Message", str(e.exception))
