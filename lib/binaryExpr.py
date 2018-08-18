#!/usr/bin/env python
# encoding: utf-8

from lib.astList import ASTList

class BinaryExpr(ASTList):
    def __init__(self, l):
        super(BinaryExpr, self).__init__(l)

    def left(self):
        return self.child(0)

    def operator(self):
        return self.child(1).token().getText()

    def right(self):
        return self.child(2)

if __name__ == '__main__':
    from numToken import NumToken
    from idToken import IdToken
    from astLeaf import ASTLeaf

    l = ASTLeaf(NumToken(1, 33))
    op = ASTLeaf(IdToken(1, '+'))
    r = ASTLeaf(NumToken(1, 66))

    be = BinaryExpr([l, op, r])

    assert be.left() == l
    assert be.operator() == "+"
    assert be.right() == r
