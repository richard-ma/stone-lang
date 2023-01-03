#!/usr/bin/env python
# encoding: utf-8

from astree import ASTree

class ASTList(ASTree):
    def __init__(self, l):
        self._children = l

    def child(self, i):
        return self._children[i]

    def numChildren(self):
        return len(self._children)

    def children(self):
        return iter(self._children) 

    def __str__(self):
        builder = list()
        builder.append('(')

        sep = ""
        for t in self._children:
            builder.append(sep)
            sep = " "
            builder.append(str(t))

        builder.append(')')

        return ''.join(builder)

    def location(self):
        for t in self._children:
            s = t.location()
            if s is not None:
                return s

        return None


if __name__ == '__main__':
    from astLeaf import ASTLeaf
    from numToken import NumToken
    nt1 = NumToken(1, 33)
    leaf1 = ASTLeaf(nt1)
    nt2 = NumToken(2, 66)
    leaf2 = ASTLeaf(nt2)
    nt3 = NumToken(3, 99)
    leaf3 = ASTLeaf(nt3)

    data = [leaf1, leaf2, leaf3]
    l = ASTList(data)

    assert l.child(2) == leaf3
    from collections.abc import Iterable # test l.children() return value is iterable
    assert isinstance(l.children(), Iterable)
    assert l.numChildren() == 3
    assert str(l) == "(33 66 99)"
    assert l.location() == "at line %d" % (1)
