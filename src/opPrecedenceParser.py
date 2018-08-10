#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lexer import *
from parseException import *
from astLeaf import ASTLeaf
from binaryExpr import BinaryExpr
from numberLiteral import NumberLiteral

class OpPrecedenceParser():

    class Precedence:
        def __init__(self, v, a):
            self.value = v
            self.leftAssoc = a

    def __init__(self, p):
        self.lexer = p
        self.operators = dict()

        self.operators["<"] = self.Precedence(1, True)
        self.operators[">"] = self.Precedence(1, True)
        self.operators["+"] = self.Precedence(2, True)
        self.operators["-"] = self.Precedence(2, True)
        self.operators["*"] = self.Precedence(3, True)
        self.operators["/"] = self.Precedence(3, True)
        self.operators["^"] = self.Precedence(4, False)

    def expression(self):
        right = self.factor()
        next = self.nextOperator()
        while next != None:
            right = self.doShift(right, next.value)
            next = self.nextOperator()

        return right

    def doShift(self, left, prec):
        op = ASTLeaf(self.lexer.read())
        right = self.factor()
        next = self.nextOperator()
        while next != None and self.rightIsExpr(prec, next):
            right = self.doShift(right, next.value)
            next = self.nextOperator()

        return BinaryExpr([left, op, right])

    def nextOperator(self):
        t = self.lexer.peek(0)
        if t.isIdentifier():
            return self.operators.get(t.getText())
        else:
            return None

    def rightIsExpr(self, prec, nextPrec):
        if nextPrec.leftAssoc:
            return prec < nextPrec.value
        else:
            return prec <= nextPrec.value

    def factor(self):
        if self.isToken("("):
            self.token("(")
            e = self.expression()
            self.token(")")
            return e
        else:
            t = self.lexer.read()
            if t.isNumber():
                n = NumberLiteral(t)
                return n
            else:
                raise ParseException(t)

    def token(self, name):
        t = self.lexer.read()
        if not (t.isIdentifier() and name == t.getText()):
            raise ParseException(t)

    def isToken(self, name):
        t = self.lexer.peek(0)
        return t.isIdentifier() and name == t.getText()


if __name__ == '__main__':

    # 合法输入
    print('parsing expression.stone')
    with open("../samples/expression.stone", 'r') as f:
        reader = LineReader(f)
        lexer = Lexer(reader)
        #token = lexer.read()
        #if token != None: print(token.getText())
        #while token != StoneToken.EOF:
            #token = lexer.read()
            #if token != None: print(token.getText())
        p = OpPrecedenceParser(lexer)

        t = p.expression()
        print("=> %s" % (t))

    # 非法输入 应该产生ParseException
    print('parsing expression_parseexception.stone')
    with open("../samples/expression_parseexception.stone", 'r') as f:
        reader = LineReader(f)
        lexer = Lexer(reader)
        #token = lexer.read()
        #if token != None: print(token.getText())
        #while token != StoneToken.EOF:
            #token = lexer.read()
            #if token != None: print(token.getText())
        p = OpPrecedenceParser(lexer)

        t = p.expression()
        print("=> %s" % (t))


