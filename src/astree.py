#!/usr/bin/env python
# encoding: utf-8

class ASTree():
    def __init__(self):
        self.l = list()

    def child(self, i):
        return self.l[i]

    def numChildren(self):
        return len(self.l)

    def children(self):
        return self.l

    def location(self):
        pass

if __name__ == "__main__":
    tree = ASTree()
    assert tree.numChildren() == 0
    assert tree.children() == list()
