#!/usr/bin/env python
# encoding: utf-8

class ASTree():
    def __init__(self):
        self.children = list()

    def child(self, i):
        return self.children[i]

    def numChildren(self):
        return len(self.children)

    def children(self):
        return self.children

    def location(self):
        pass

    #def iterator(self):
        #return self.children()
