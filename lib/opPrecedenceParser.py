#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.lexer import *
from lib.parseException import *
from lib.astLeaf import ASTLeaf
from lib.binaryExpr import BinaryExpr
from lib.numberLiteral import NumberLiteral

class OpPrecedenceParser():

    class Precedence:
        def __init__(self, v, a):
            self.value = v # 优先级，数字越大优先级越高
            self.leftAssoc = a # 该运算符是否为左结合

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
        op = ASTLeaf(self.lexer.read()) # 读入操作符
        right = self.factor() # 读入右侧的factor
        next = self.nextOperator() # 获得下一个操作符
        while next != None and self.rightIsExpr(prec, next):
            right = self.doShift(right, next.value)
            next = self.nextOperator()

        return BinaryExpr([left, op, right])

    def nextOperator(self):
        t = self.lexer.peek(0) # 获取下一个词
        if t.isIdentifier(): # 是标识符的话，返回标识符的优先级和结合性质
            return self.operators.get(t.getText())
        else:
            return None # 返回None说明没有下一个操作符了，这个操作符是最右侧的了

    def rightIsExpr(self, prec, nextPrec):
        if nextPrec.leftAssoc:
            return prec < nextPrec.value # 2 + 3 * 5: 3 * 5是一个右侧的表达式
        else:
            return prec <= nextPrec.value # 2 ^ 3 ^ 7: ^幂运算符是右结合的，所以这时候右侧(3 ^ 7)是表达式

    def factor(self):
        if self.isToken("("): # "(" expression ")"
            self.token("(")
            e = self.expression()
            self.token(")")
            return e
        else: # NUMBER
            t = self.lexer.read()
            if t.isNumber():
                n = NumberLiteral(t)
                return n
            else:
                raise ParseException(t)

    def token(self, name): # 读入的字符是标识符name
        t = self.lexer.read()
        if not (t.isIdentifier() and name == t.getText()):
            raise ParseException(t)

    def isToken(self, name): # 判断下一个字符是否为标识符name
        t = self.lexer.peek(0)
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
        p = OpPrecedenceParser(lexer)

        t = p.expression()
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
        p = OpPrecedenceParser(lexer)

        t = p.expression()
        print("=> %s" % (t))


