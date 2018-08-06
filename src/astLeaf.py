#!/usr/bin/env python
# encoding: utf-8

from astree import ASTree
from stoneToken import StoneToken

class ASTLeaf(ASTree):
    def __ini__(self, token):
        self.empty = list()
        self.token = token

    def child(self, i):
        pass

    def numChildren(self):
        return 0

    def children(self):
        return empty

    def __str__(self):
        return self.token.getText()

    def location(self):
        return "at line " + self.token.getLineNumber()

    def token(self):
        return self.token
