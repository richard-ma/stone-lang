#!/usr/bin/env python
# encoding: utf-8

from collections import deque
from astree import ASTree

class ASTLeaf(ASTree):
    def __init__(self, token):
        self._empty = deque()
        self._token = token

    def child(self, i):
        # throw Exception
        raise NotImplementedError()

    def numChildren(self):
        return 0 # num of children is 0

    def children(self):
        return iter(self._empty)

    def __str__(self):
        return self._token.getText()

    def location(self):
        return "at line " + str(self._token.getLineNumber())

    def token(self):
        return self._token


if __name__ == '__main__':
    from numToken import NumToken
    token = NumToken(1, 33)
    leaf = ASTLeaf(token)

    assert str(leaf) == "33"
    assert leaf.location() == "at line %d" % (1)
    assert leaf.token() == token
