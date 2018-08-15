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
        return None

    # 书中实现了java的iterable接口
    # 添加此方法用于向内部添加child
    def add(self, child):
        self.l.append(child)

if __name__ == "__main__":
    tree = ASTree()
    assert tree.numChildren() == 0
    assert tree.children() == list()
