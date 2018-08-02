#!/usr/bin/env python
# encoding: utf-8

from stoneToken import StoneToken

class StrToken(StoneToken):
    def __init__(self, line, string):
        super(StrToken, self).__init__(line)
        self.literal = string

    def isString(self):
        return True

    def getText(self):
        return self.literal

if __name__ == '__main__':
    st = StrToken(1, 'literal')

    assert st.isNumber() == False
    assert st.isIdentifier() == False
    assert st.isString() == True
    assert st.getText() == "literal"
