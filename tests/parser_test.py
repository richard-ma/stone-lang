#!/usr/bin/env python
# encoding: utf-8

import unittest
from random import randint
from random import choice

from lib.parser import *
from lib.astree import *
from lib.astList import *
from lib.astLeaf import *
from lib.binaryExpr import *
from lib.numberLiteral import *
from lib.name import *

class TestParser_Element(unittest.TestCase):

    """Test case docstring."""

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
        p = Parser(NumberLiteral)
        self.assertIsInstance(p, Parser)

        q = Parser(p)
        self.assertIsInstance(q, Parser)

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

class TestParser_Skip(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.value = 'hello'
        self.token = IdToken(self.lineNumber, self.value)

    def tearDown(self):
        pass

    def test_init(self):
        s = Parser.Skip(self.token)
        self.assertIsInstance(s, Parser.Skip)
        self.assertIsInstance(s, Parser.Leaf)

    def test_find(self):
        s = Parser.Skip(self.token)
        self.assertEqual(None, s.find(list(), self.token))


class TestParser_Precedence(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.v = randint(1, 10)
        self.a = choice([True, False])

    def tearDown(self):
        pass

    def test_init(self):
        p = Parser.Precedence(self.v, self.a)
        self.assertEqual(self.v, p.value)
        self.assertEqual(self.a, p.leftAssoc)


class TestParser_AToken(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        pass

class TestParser_IdToken(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.value = 'hello'
        self.token = IdToken(self.lineNumber, self.value)

    def tearDown(self):
        pass

    def test_init(self):
        token = Parser.IdToken(Name)
        self.assertIsInstance(token, Parser.IdToken)

    def test_test(self):
        token = Parser.IdToken(Name)
        result = token.test(self.token)
        self.assertEqual(result, True)

class TestParser_NumToken(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.value = 33
        self.token = NumToken(self.lineNumber, self.value)

    def tearDown(self):
        pass

    def test_init(self):
        token = Parser.NumToken(NumberLiteral)
        self.assertIsInstance(token, Parser.NumToken)

    def test_test(self):
        token = Parser.NumToken(NumberLiteral)
        result = token.test(self.token)
        self.assertEqual(result, True)

class TestParser_StrToken(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = randint(1, 10)
        self.value = 'hello'
        self.token = StrToken(self.lineNumber, self.value)

    def tearDown(self):
        pass

    def test_init(self):
        token = Parser.StrToken(Name)
        self.assertIsInstance(token, Parser.StrToken)

    def test_test(self):
        token = Parser.StrToken(Name)
        result = token.test(self.token)
        self.assertEqual(result, True)


class TestParser_Factory(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.lineNumber = 1
        self.value = 33
        self.text = "text"
        self.stoneToken = StoneToken(self.lineNumber)
        self.idToken = IdToken(self.lineNumber, self.text)
        self.strToken = StrToken(self.lineNumber, self.text)
        self.numToken = NumToken(self.lineNumber, self.value)

    def tearDown(self):
        pass

    def test_FACTORYNAME_not_none(self):
        self.assertNotEqual(Parser.Factory.FACTORY_NAME, None)

    def test_get(self):
        factory = Parser.Factory.get(ASTLeaf)
        instance = factory.make(self.numToken)
        self.assertIsInstance(instance, ASTree)

        factory = Parser.Factory.get(ASTLeaf)
        instance = factory.make(self.strToken)
        self.assertIsInstance(instance, ASTree)

    def test_getForASTList(self):
        # only one item in list
        factory = Parser.Factory.getForASTList(ASTList)
        instance = factory.make([self.numToken])
        self.assertIsInstance(instance, ASTree)

        # many items in list
        factory = Parser.Factory.getForASTList(ASTList)
        instance = factory.make([self.numToken, self.strToken])
        self.assertIsInstance(instance, ASTree)

class TestParser(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.p = Parser(NumberLiteral)
        self.q = Parser(self.p)

    def tearDown(self):
        pass

    def test_init_with_None(self):
        parser = Parser(None)
        self.assertIsInstance(parser.elements, list)
        self.assertEqual(0, len(parser.elements))

    def test_init_with_ASTree_subclass(self):
        self.assertIsInstance(self.p.elements, list)
        self.assertIsInstance(self.p.factory, Parser.Factory)
        self.assertEqual(0, len(self.p.elements))

    def test_init_with_Parser(self):
        self.assertIsInstance(self.q.elements, list)
        self.assertIsInstance(self.q.factory, Parser.Factory)
        self.assertEqual(len(self.p.elements), len(self.q.elements))

    def test_rule_with_none(self):
        self.assertIsInstance(Parser.rule(), Parser)

    def test_rule_with_parser(self):
        self.assertIsInstance(Parser.rule(NumberLiteral), Parser)

    def test_reset_with_none(self):
        ret = self.p.reset()  # invoke reset
        self.assertIsInstance(ret, Parser)  # return type is Parser
        self.assertEqual(0, len(self.p.elements))

    def test_reset_with_ASTree_subclass(self):
        ret = self.p.reset(NumberLiteral)  # invoke reset
        self.assertIsInstance(ret, Parser)  # return type is Parser
        self.assertEqual(0, len(self.p.elements))
        self.assertIsInstance(self.p.factory, Parser.Factory)

if __name__ == '__main__':
    unittest.main()
