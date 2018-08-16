#!/usr/bin/env python
# encoding: utf-8

from abc import *

class ASTree(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def child(self, i):
        pass

    @abstractmethod
    def numChildren(self):
        pass

    @abstractmethod
    def children(self):
        pass

    @abstractmethod
    def location(self):
        pass

    @abstractmethod
    def add(self, child):
        pass

if __name__ == '__main__':
    a = ASTree() # TypeError
