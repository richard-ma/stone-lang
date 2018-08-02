#!/usr/bin/env python
# encoding: utf-8

from stoneException import StoneException
from stoneToken import StoneToken
from numToken import NumToken

class ParseException(Exception):
    def __init__(self, t, msg = ''):
        super(ParseException, self).__init__()
        self.errmsg = "syntax error around " + self.location(t) + ". " + msg

    def __str__(self):
        return self.errmsg

    def location(self, t):
        if t == StoneToken.EOF:
            return "the last line"
        else:
            return "\"" + t.getText() + "\" at line " + str(t.getLineNumber())

# Testing and Usage
if __name__ == '__main__':
    try:
        nt = NumToken(33, 123)
        raise ParseException(nt, "[error message]")
    except ParseException as e:
        print(e)
        raise
