#!/usr/bin/env python
# encoding: utf-8

import unittest
from random import randint

from lib.parser import *
from lib.astree import *
from lib.astList import *
from lib.astLeaf import *
from lib.binaryExpr import *
from lib.numberLiteral import *
from lib.name import *
from lib.idToken import IdToken

class TestParser_Element(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        with self.assertRaises(TypeError):
            Parser.Element()

class TestParser_Tree(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        with self.assertRaises(TypeError):
            Parser.Tree(1) # parameter must be instance of Parser

class TestParser_OrTree(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        with self.assertRaises(TypeError):
            Parser.OrTree(1) # parameter must be instance of Parser

class TestParser_Repeat(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        with self.assertRaises(TypeError):
            Parser.Repeat(1, True) # parameter must be instance of Parser
        with self.assertRaises(TypeError):
            Parser.Repeat(1, 1)

class TestParser_AToken(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        atoken = AToken()

class TestParser_IdToken(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.value = ';'
        self.token = IdToken(self.lineNumber, self.value)

    def tearDown(self):
        pass

    def test_name(self):
        pass

class TestParser_Factory(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = 1
        self.value = 33
        self.text = "text"
        self.idToken = IdToken(self.lineNumber, self.text)
        self.strToken = StrToken(self.lineNumber, self.text)
        self.numToken = NumToken(self.lineNumber, self.value)

    def tearDown(self):
        pass

    def test_get(self):
        instance = Parser.Factory.get(NumberLiteral).make(self.numToken)
        self.assertIsInstance(instance, ASTree)
        self.assertEqual(instance.value(), self.value)

        instance = Parser.Factory.get(Name).make(self.strToken)
        self.assertIsInstance(instance, ASTree)
        self.assertEqual(instance.name(), self.text)

    def test_getForASTList(self):
        instance = Parser.Factory.getForASTList(ASTList).make([NumberLiteral(self.numToken)])
        self.assertIsInstance(instance, ASTree)
        self.assertIsInstance(instance, NumberLiteral)

        instance = Parser.Factory.getForASTList(ASTList).make([NumberLiteral(self.numToken), Name(self.strToken)])
        self.assertIsInstance(instance, ASTree)
        self.assertIsInstance(instance, ASTList)

class TestParser(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.p = Parser(NumberLiteral)
        self.q = Parser(self.p)

    def tearDown(self):
        pass

    def test_init_with_ASTree_subclass(self):
        self.assertIsInstance(self.p.elements, list)
        self.assertIsInstance(self.p.factory, Parser.Factory)
        self.assertEqual(0, len(self.p.elements))

    def test_init_with_Parser(self):
        self.assertIsInstance(self.q.elements, list)
        self.assertIsInstance(self.q.factory, Parser.Factory)
        self.assertEqual(0, len(self.q.elements))

    def test_reset_with_none(self):
        ret = self.p.reset()  # invoke reset
        self.assertIsInstance(ret, Parser)  # return type is Parser
        self.assertEqual(0, len(self.p.elements))

    def test_reset_with_ASTree_subclass(self):
        ret = self.p.reset(NumberLiteral)  # invoke reset
        self.assertIsInstance(ret, Parser)  # return type is Parser
        self.assertEqual(0, len(self.p.elements))
        self.assertIsInstance(self.p.factory)

if __name__ == '__main__':
    unittest.main()
