#!/usr/bin/env python
# encoding: utf-8

from stoneToken import StoneToken

class ParseException(Exception):
    def __init__(self, t, msg = ''):
        super(ParseException, self).__init__()
        self.errmsg = "syntax error around " + self.location(t) + ". " + msg

    def location(self, t):
        if t == StoneToken.EOF:
            return "the last line"
        else:
            return "\"" + t.getText() + "\" at line " + str(t.getLineNumber())

    def __str__(self):
        return self.errmsg

# Testing and Usage
if __name__ == '__main__':
    from lib.numToken import NumToken
    try:
        nt = NumToken(33, 123)
        raise ParseException(nt, "[error message]")
    except ParseException as e:
        print(e)
        print(e.location(nt))