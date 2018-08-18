#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint
import io

from lib.lexer import *

class TestLineReader(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        # fake input file
        # https://stackoverflow.com/questions/11833428/how-to-create-fake-text-file-in-python
        # https://docs.python.org/3/library/io.html#io.StringIO
        self.f = io.StringIO()
        self.lines = ['First line\n', 'Second line\n', 'Third line\n']
        self.f.write(''.join(self.lines))
        # StringIO need reset file pointer to call readline()
        # https://bytes.com/topic/python/answers/478319-stringio-readline-returns
        self.f.seek(0)
        self.lineReader = LineReader(self.f)

    def tearDown(self):
        # close fake input file
        self.f.close()

    def test_getLineNumber(self):
        self.assertEqual(0, self.lineReader.getLineNumber())

    def test_readline(self):
        for idx in range(len(self.lines)):
            self.assertEqual(self.lines[idx], self.lineReader.readline())
            self.assertEqual(idx + 1, self.lineReader.getLineNumber())

        self.assertIsNone(self.lineReader.readline())
        self.assertEqual(len(self.lines), self.lineReader.getLineNumber())

class TestLexer(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
