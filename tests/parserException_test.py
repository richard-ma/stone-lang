#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint

from lib.parseException import ParseException
from lib.numToken import NumToken
from lib.stoneToken import StoneToken

class TestParserException(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.value = randint(1, 100)
        self.token = NumToken(self.lineNumber, self.value)
        self.EOFToken = StoneToken.EOF

    def tearDown(self):
        pass

    def test_location(self):
        pe = ParseException(self.token, "error message")
        self.assertEqual("\"%s\" at line %d" % (self.token.getText(), self.lineNumber),
                pe.location(self.token))

        self.assertEqual("the last line",
                pe.location(self.EOFToken))

    def test_parserException(self):
        with self.assertRaises(ParseException) as e:
            raise ParseException(self.token, "error message")

        self.assertEqual(
                "syntax error around \"%s\" at line %d. error message" % (self.token.getText(), self.lineNumber),
                str(e.exception))

    def test_parserExceptionLastLine(self):
        with self.assertRaises(ParseException) as e:
            raise ParseException(self.EOFToken, "error message")

        self.assertEqual(
                "syntax error around the last line. error message",
                str(e.exception))

if __name__ == '__main__':
    unittest.main()
