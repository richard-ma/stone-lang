#!/usr/bin/env python
# encoding: utf-8

from lib.stoneToken import StoneToken

class IdToken(StoneToken):
    def __init__(self, line, id):
        super(IdToken, self).__init__(line)
        self.text = id

    def isIdentifier(self):
        return True

    def getText(self):
        return self.text

if __name__ == '__main__':
    it = IdToken(1, 'identifier')

    assert it.isNumber() == False
    assert it.isString() == False
    assert it.isIdentifier() == True
    assert it.getText() == "identifier"
