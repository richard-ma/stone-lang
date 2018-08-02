#!/usr/bin/env python
# encoding: utf-8

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
        pass

    def getText(self):
        return ""

if __name__ == '__main__':
    t = StoneToken(3)
    print(t)
