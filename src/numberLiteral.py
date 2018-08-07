#!/usr/bin/env python
# encoding: utf-8

from astLeaf import ASTLeaf

class NumberLiteral(ASTLeaf):
    def __init__(self, token):
        super(NumberLiteral, self).__init__(token)

    def value(self):
        return self.token().getNumber()

if __name__ == '__main__':
    from numToken import NumToken
    token = NumToken(1, 33)
    nl = NumberLiteral(token)

    assert nl.value() == 33
