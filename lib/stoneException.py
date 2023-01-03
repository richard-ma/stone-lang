#!/usr/bin/env python
# -*- coding: utf-8 -*-

class StoneException(Exception):
    # TODO: ADD AST tree initial object
    def __init__(self, errmsg, t=None):
        if t is None:
            super(StoneException, self).__init__()
            self.errmsg = errmsg
        else:
            pass # ASTtree is not None

    def __str__(self):
        return self.errmsg

# Testing and Usage
if __name__ == '__main__':
    try:
        raise StoneException("This is a StoneException")
    except StoneException as e:
        print(e)
        raise
