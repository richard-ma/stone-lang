#!/usr/bin/env python
# encoding: utf-8

from astree import ASTree
from stoneToken import StoneToken

class ASTLeaf(ASTree):
    def __init__(self, t):
        self.empty = list()
        self.t = t

    def child(self, i):
        # throw Exception
        return None

    def numChildren(self):
        return 0

    def children(self):
        # return empty list
        # OR throw Exception
        return empty

    def __str__(self):
        return self.t.getText()

    def location(self):
        return "at line " + str(self.t.getLineNumber())

    def token(self):
        return self.t

if __name__ == '__main__':
    from numToken import NumToken
    token = NumToken(1, 33)
    leaf = ASTLeaf(token)

    assert leaf.numChildren() == 0
    assert str(leaf) == "33"
    assert leaf.location() == "at line %d" % (1)
    assert leaf.token() == token
