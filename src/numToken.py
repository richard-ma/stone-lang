#!/usr/bin/env python
# encoding: utf-8

from stoneToken import StoneToken

class NumToken(StoneToken):
    def __init__(self, line, value):
        super(NumToken, self).__init__(line)
        self.value = value

    def isNumber(self):
        return True

    def getText(self):
        return str(self.value)

    def getNumber(self):
        return self.value

if __name__ == '__main__':
    nt = NumToken(1, 33)

    assert nt.isNumber() == True
    assert nt.getText() == "33"
    assert nt.getNumber() == 33
