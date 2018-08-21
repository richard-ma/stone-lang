#!/usr/bin/env python
# encoding: utf-8

from abc import *

class Parser():
    class Element(ABC):
        @abstractmethod
        def parse(self, lexer, res):
            pass

        @abstractmethod
        def match(self, lexer):
            pass

'''
from parseException import ParseException
from astList import ASTList
from astLeaf import ASTLeaf

class Tree(Element):
    def __init__(self, parser):
        self.parser = parser

    def parse(self, lexer, res):
        res.add(self.parser.parse(lexer))

    def match(self, lexer):
        return self.parser.match(lexer)

class OrTree(Element):
    def __init__(self, p):
        self.parsers = p

    def parse(self, lexer, res):
        p = self.choose(lexer)
        if p == None:
            raise ParseException(lexer.peek(0))
        else:
            res.add(p.parse(lexer))

    def match(self, lexer):
        return self.choose(lexer) != None

    def choose(self, lexer):
        for p in self.parsers:
            if p.match(lexer):
                return p
        return None

    def insert(self, p):
        self.parsers = [p] + self.parsers

class Repeat(Element):
    def __init__(self, p, once):
        self.parser = p
        self.onlyOnce = once

    def parse(self, lexer, res):
        while self.parser.match(lexer):
            t = self.parser.parse(lexer)
            if instanceof(t, ASTList) or t.numChildren() > 0:
                res.add(t)
            if self.onlyOnce:
                break

    def match(self, lexer):
        return self.parser.match(lexer)

class AToken(Element):
    def __init__(self, t):
        self.factory = Factory()
        if t is None:
            t = eval(ASTLeaf.__name__)
            factory = self.factory.get(t, StoneToken.__name__)

    def parse(self, lexer, res):
        t = lexer.read()
        if self.test(t):
            leaf = self.factory.make(t)
            res.add(leaf)
        else:
            raise parseException(t)

    def match(self, lexer):
        return self.test(lexer.peek(0))

    def test(self, t):
        pass

class AIdToken(AToken):
    def __init__(self, t, r):
        super(AIdToken, self).__init__(t)
        self.reserved = r if r != None else dict()

    def test(self, t):
        return t.isIdentifier() and not t.getText() in self.reserved

class ANumToken(AToken):
    def __init__(self, t):
        super(ANumToken, self).__init__(t)

    def test(self, t):
        return t.isNumber();

class AStrToken(AToken):
    def __init__(self, t):
        super(AStrToken, self).__init__(t)

    def test(self, t):
        return t.isString()

class Leaf(Element):
    def __init__(self, pat):
        self.tokens = pat

    def parse(self, lexer, res):
        t = lexer.read()
        if t.isIdentifier():
            for token in self.tokens:
                if token == t.getText():
                    self.find(res, t)
                    return

        if len(tokens) > 0:
            raise ParseException(tokens[0] + " expected.", t)
        else:
            raise ParseException(t)

    def find(self, res, t):
        res.add(ASTLeaf(t))

    def match(self, lexer):
        t = lexer.peek(0)
        if t.isIdentifier():
            for token in self.tokens:
                if token == t.getText():
                    return True

        return False

class Skip(Leaf):
    def __init__(self, t):
        super(Skip, self).__init__(t)

    def find(self, res, t):
        pass

class Precedence:
    def __init__(self, v, a):
        self.value = v
        self.leftAssoc = a

# Extend dict class
# https://stackoverflow.com/questions/2328235/pythonextend-the-dict-class
class Operators(dict):
    LEFT = True
    RIGHT = False

    def __init__(self, *args, **kw):
        super(Operators, self).__init__(*args, **kw)

    def add(name, perc, leftAssoc):
        super(Operators, self).__setitem__(name, Precedence(prec, leftAssoc))

class Expr(Element):
    def __init__(self, clazz, exp, m):
        self.factory = Factory.getForASTList(clazz)
        self.ops = m
        self.factor = exp

    def parse(self, lexer, res):
        right = self.factor.parse(lexer)
        prec = None
        while (prec = nextOperator(lexer)) != None:
            right = doShift(lexer, right, prec.value)

        res.add(right)

    def doShift(self, lexer, left, prec):
        l = list()
        l.append(left)
        l.append(ASTLeaf(lexer.read()))
        right = factor.parse(lexer)
        while (n = nextOperator(lexer)) != None and rightIsExpr(prec, n):
            right = doShift(lexer, right, n.value)
        l.append(right)
        return self.factory.make(l)

    def nextOperator(self, lexer):
        t = lexer.peek(0)
        if t.isIdentifier():
            return ops.get(t.getText())
        else:
            return None

    def rightIsExpr(self, prec, nextPrec):
        if nextPrec.leftAssoc:
            return prec < nextPrec.value
        else:
            return prec <= nextPrec.value

    def match(self, lexer):
        return self.factory.match(lexer)

class Factory():
    def make0(self):
        pass

    def make(self, arg):
        try:
            return make0(arg)
        except Exception as e:
            raise e

    def getForASTList(self, clazz):
        pass
        #f = get(clazz, list)
        #if f == None:
            #f = Factory()



class Parser():
    pass
'''
