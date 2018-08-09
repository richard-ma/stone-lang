#!/usr/bin/env python
# encoding: utf-8

from parseException import ParseException
from astList import ASTList

class Element():
    def parse(self, lexer, res):
        pass

    def match(self, lexer):
        pass

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
        if t is None:
            t = ASTLeaf.__name__
            factory = self.factory.get(t, StoneToken.__name__)

class Parser():
    pass
