#!/usr/bin/env python
# encoding: utf-8

from astLeaf import ASTLeaf

class Name(ASTLeaf):
    def __init__(self, token):
        super(Name, self).__init__(token)

    def name(self):
        return self.token().getText()

if __name__ == '__main__':
    from strToken import StrToken

    s = StrToken(1, "hello")
    n = Name(s)
    assert n.name() == "hello"
