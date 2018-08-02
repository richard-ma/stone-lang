#!/usr/bin/env python
# encoding: utf-8

from stoneException import StoneException

class StoneToken():
    def __init__(self, line):
        #self.EOF = Token(-1)
        self.EOL = "\\n"
        self.lineNumber = line

    def getLineNumber(self):
        return self.lineNumber

    def isIdentifier(self):
        return False

    def isNumber(self):
        return False

    def isString(self):
        return False

    def getNumber(self):
        raise StoneException("not number token")

    def getText(self):
        return ""

# Testing and Usage
if __name__ == '__main__':
    t = StoneToken(3)
    print(t.getLineNumber())
    print(t.isIdentifier())
    print(t.isNumber())
    print(t.isString())
    print(t.getText())
    print(t.getNumber())
