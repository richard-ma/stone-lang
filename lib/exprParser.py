#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.lexer import *
from lib.parseException import *
from lib.astLeaf import ASTLeaf
from lib.binaryExpr import BinaryExpr
from lib.numberLiteral import NumberLiteral

class ExprParser():
    def __init__(self, p):
        if isinstance(p, Lexer):
            self.lexer = p
        else:
            raise Exception('need Lexer instance, But param is %s' % (type(p).__name__))

    def expression(self):
        left = self.term()
        while self.isToken("+") or self.isToken("-"):
            op = ASTLeaf(lexer.read())
            right = self.term()
            left = BinaryExpr([left, op, right])
        return left

    def term(self):
        left = self.factor()
        while self.isToken("*") or self.isToken("/"):
            op = ASTLeaf(lexer.read())
            right = self.factor()
            left = BinaryExpr([left, op, right])
        return left

    def factor(self):
        if self.isToken("("):
            self.token("(")
            e = self.expression()
            self.token(")")
            return e
        else:
            t = lexer.read()
            if t.isNumber():
                n = NumberLiteral(t)
                return n
            else:
                raise ParseException(t)

    def token(self, name):
        t = lexer.read()
        if not (t.isIdentifier() and name == t.getText()):
            raise ParseException(t)

    def isToken(self, name):
        t = lexer.peek(0)
        return t.isIdentifier() and name == t.getText()

if __name__ == '__main__':

    # 合法输入
    print('parsing expression.stone')
    with open("samples/expression.stone", 'r') as f:
        reader = LineReader(f)
        lexer = Lexer(reader)
        #token = lexer.read()
        #if token != None: print(token.getText())
        #while token != StoneToken.EOF:
            #token = lexer.read()
            #if token != None: print(token.getText())
        ep = ExprParser(lexer)

        t = ep.expression()
        print("=> %s" % (t))

    # 非法输入 应该产生ParseException
    print('parsing expression_parseexception.stone')
    with open("samples/expression_parseexception.stone", 'r') as f:
        reader = LineReader(f)
        lexer = Lexer(reader)
        #token = lexer.read()
        #if token != None: print(token.getText())
        #while token != StoneToken.EOF:
            #token = lexer.read()
            #if token != None: print(token.getText())
        ep = ExprParser(lexer)

        t = ep.expression()
        print("=> %s" % (t))


