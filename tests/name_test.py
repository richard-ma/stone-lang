#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint

from lib.name import Name
from lib.strToken import StrToken

class TestName(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.string = 'hello'
        self.token = StrToken(self.lineNumber, self.string)
        self.n = Name(self.token)

    def tearDown(self):
        pass

    def test_name(self):
        self.assertEqual(self.string, self.n.name())

if __name__ == '__main__':
    unittest.main()
