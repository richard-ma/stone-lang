#!/usr/bin/env python
# encoding: utf-8

from abc import *
from types import FunctionType

from lib.lexer import *
from lib.astree import *
from lib.astList import *
from lib.astLeaf import *


class Parser():
    # 基类
    class Element(ABC):
        @abstractmethod
        def parse(self, lexer, res):
            pass

        @abstractmethod
        def match(self, lexer):
            pass

    # 表达式实现
    class Tree(Element):
        def __init__(self, parser):
            if not isinstance(parser, Parser):
                raise TypeError()

            self.parser = parser

        def parse(self, lexer, res):
            if not all([
                isinstance(lexer, Lexer),
                isinstance(res, list)
            ]):
                raise TypeError()

            res.add(self.parser.parse(lexer))

        def match(self, lexer):
            if not isinstance(lexer, Lexer):
                raise TypeError()

            return self.parser.match(lexer)

    class OrTree(Element):
        def __init__(self, parsers):
            if not isinstance(parsers, list):
                raise TypeError()

            self.parsers = parsers

        def parse(self, lexer, res):
            if not all([
                    isinstance(lexer, Lexer),
                    isinstance(res, list)
            ]):
                raise TypeError()

            p = self.choose(lexer)
            if p == None:
                raise ParseException(lexer.peek(0))
            else:
                res.add(p.parse(lexer))

        def match(self, lexer):
            if not isinstance(lexer, Lexer):
                raise TypeError()

            return self.choose(lexer) != None

        # 遍历Parsers，有可以匹配的就返回
        def choose(self, lexer):
            if not isinstance(lexer, Lexer):
                raise TypeError()

            for p in self.parsers:
                if p.match(lexer):
                    return p
            return None

        # 添加parser
        def insert(self, parser):
            if not isinstance(parser, Parser):
                raise TypeError()

            self.parsers = [parser] + self.parsers

    class Repeat(Element):
        def __init__(self, parser, once):
            if not all([
                    isinstance(parser, Parser),
                    isinstance(once, bool)
            ]):
                raise TypeError()

            self.parser = parser
            self.onlyOnce = once

        def parse(self, lexer, res):
            if not all([
                    isinstance(lexer, Lexer),
                    isinstance(res, list)
            ]):
                raise TypeError()

            while self.parser.match(lexer):
                t = self.parser.parse(lexer)
                if not isinstance(t, ASTList) or t.numChildren() > 0:
                    res.add(t)
                if self.onlyOnce:
                    break

        def match(self, lexer):
            if not isinstance(lexer, Lexer):
                raise TypeError()

            return self.parser.match(lexer)

    # 终结符父类
    class AToken(Element):
        def __init__(self, t):
            if t is None:
                t = ASTLeaf

            if issubclass(t, ASTLeaf):
                self.factory = Parser.Factory.get(t)

        def parse(self, lexer, res):
            if not all([
                    isinstance(lexer, Lexer),
                    isinstance(res, list)
            ]):
                raise TypeError()

            t = lexer.read()
            if self.test(t):
                leaf = self.factory.make(t)  # 根据符号创建语法树对象
                res.add(leaf)
            else:
                raise ParseException(t)

        def match(self, lexer):
            return self.test(lexer.peek(0))

        # 验证符号是否为该类型
        @abstractmethod
        def test(self, t):
            pass

    # ID终结符
    class IdToken(AToken):
        def __init__(self, t, r=None):
            if not issubclass(t, ASTLeaf):
                raise TypeError()

            super().__init__(t)
            self.reserved = r if r != None else dict()

        def test(self, t):
            return t.isIdentifier() and not t.getText() in self.reserved

    # 数值终结符
    class NumToken(AToken):
        def __init__(self, t):
            super().__init__(t)

        def test(self, t):
            return t.isNumber()

    # 字符串终结符
    class StrToken(AToken):
        def __init__(self, t):
            super().__init__(t)

        def test(self, t):
            return t.isString()

    class Leaf(Element):
        def __init__(self, pat):
            if not isinstance(pat, list):
                raise TypeError()

            self.tokens = pat

        def parse(self, lexer, res):
            if not all([
                isinstance(lexer, Lexer),
                isinstance(res, list)
            ]):
                raise TypeError()

            t = lexer.read()
            if t.isIdentifier():
                for token in self.tokens:
                    if token == t.getText():
                        self.find(res, t)
                        return

            if len(self.tokens) > 0:
                raise ParseException(self.tokens[0] + " excepted.", t)
            else:
                raise ParseException(t)

        def find(self, res, t):
            if not all([
                isinstance(res, list),
                isinstance(t, StoneToken)
            ]):
                raise TypeError()

            res.add(ASTLeaf(t))

        def match(self, lexer):
            if not isinstance(lexer, Lexer):
                raise TypeError()

            t = lexer.peek(0)
            if t.isIdentifier():
                for token in self.tokens:
                    if token == t.getText():
                        return True

            return False

    class Skip(Leaf):
        def __init__(self, t):
            super().__init__(t)

        def find(self, res, t):
            if not all([
                    isinstance(res, list),
                    isinstance(t, StoneToken)
            ]):
                raise TypeError()

    class Precedence():
        def __init__(self, v, a):
            if not all([
                    isinstance(v, int),
                    isinstance(a, bool)
            ]):
                raise TypeError()

            self.value = v
            self.leftAssoc = a

    # 创建ASTree类型及子类型的工厂
    class Factory():
        FACTORY_NAME = 'create'

        @abstractmethod
        def make0(self, arg):
            pass

        def make(self, arg):
            try:
                return self.make0(arg)
            except ValueError as e:
                raise e
            except Exception as e:
                raise RuntimeError(e)  # compiler ERROR

        @staticmethod
        def get(cls):  # python don't need arguments of method rewrite
            if not issubclass(cls, ASTree):
                raise TypeError()

            if cls is None:
                return None

            try:
                # 使用create方法创建instance
                m = getattr(cls, Parser.Factory.FACTORY_NAME)

                def make0(self, arg):
                    return m(arg)

                f = Parser.Factory()
                f.make0 = make0.__get__(f, Parser.Factory)  # bind make0 to f instance

                return f

            except AttributeError:  # not found method which named create in argType class
                pass

            # use default constructor
            try:
                def make0(self, arg):
                    return cls(arg)

                f = Parser.Factory()
                f.make0 = make0.__get__(f, Parser.Factory)

                return f

            except Exception as e:
                raise RuntimeError(e)

        @staticmethod
        def getForASTList(cls):
            f = Parser.Factory.get(cls)

            if f is None:
                def make0(self, arg):
                    results = arg
                    if len(results) == 1:
                        return results.get(0)
                    else:
                        return ASTList(results)

                f = Parser.Factory()
                f.make0 = make0.__get__(f, Parser.Factory)

            return f

    ###############################################################################
    # Class Parser Method
    ###############################################################################
    def __init__(self, arg):
        if arg is None:
            cls = arg
            self.reset(cls)
        elif isinstance(arg, Parser):
            p = arg
            self.elements = p.elements
            self.factory = p.factory
        elif issubclass(arg, ASTree):
            cls = arg
            self.reset(cls)
        else:
            raise TypeError()

    def parse(self, lexer):
        if not isinstance(lexer, Lexer):
            raise TypeError()

        results = list()
        for e in self.elements:
            e.parse(lexer, results)

        return self.factory.make(results)

    @staticmethod
    def rule(cls=None):
        if issubclass(cls, ASTree) or cls is None:
            return Parser(cls)
        else:
            raise TypeError()

    def reset(self, cls=None):
        if cls is None:
            self.elements = list()
            return self
        elif issubclass(cls, ASTree):
            self.elements = list()
            self.factory = Parser.Factory.getForASTList(cls)
            return self
        else:
            raise TypeError()

    def number(self, cls=None):
        if issubclass(cls, ASTLeaf):
            self.elements.add(NumToken(cls))
        else:
            raise TypeError()


###############################################################################
# Class Parser Method End
###############################################################################

'''
    def match(self, lexer):
        if not isinstance(lexer, Lexer):
            raise TypeError()

        if (len(self.elements)) == 0:
            return True
        else:
            e = self.elements.get(0)
            return e.match(lexer)

if __name__ == '__main__':
    print(globals())

    # 合法输入
    #print('parsing expression.stone')
    #with open("samples/expression.stone", 'r') as f:
        #reader = LineReader(f)
        #lexer = Lexer(reader)
        #res = ASTree()
        #atoken = Parser.ANumToken()
        #atoken.parse(lexer, res)

        #print("=> %s" % (res))

    # 非法输入 应该产生ParseException
    #print('parsing expression_parseexception.stone')
    #with open("samples/expression_parseexception.stone", 'r') as f:
        #reader = LineReader(f)
        #lexer = Lexer(reader)
        ##token = lexer.read()
        ##if token != None: print(token.getText())
        ##while token != StoneToken.EOF:
            ##token = lexer.read()
            ##if token != None: print(token.getText())
        #p = OpPrecedenceParser(lexer)

        #t = p.expression()
        #print("=> %s" % (t))


from parseException import ParseException
from astList import ASTList
from astLeaf import ASTLeaf
class Leaf(Element):
    def __init__(self, pat):
        self.tokens = pat

    def parse(self, lexer, res):
        t = lexer.read()
        if t.isIdentifier():
            for token in self.tokens:
                if token == t.getText():
                    self.find(res, t)
                    return

        if len(tokens) > 0:
            raise ParseException(tokens[0] + " expected.", t)
        else:
            raise ParseException(t)

    def find(self, res, t):
        res.add(ASTLeaf(t))

    def match(self, lexer):
        t = lexer.peek(0)
        if t.isIdentifier():
            for token in self.tokens:
                if token == t.getText():
                    return True

        return False

class Skip(Leaf):
    def __init__(self, t):
        super(Skip, self).__init__(t)

    def find(self, res, t):
        pass

class Precedence:
    def __init__(self, v, a):
        self.value = v
        self.leftAssoc = a

# Extend dict class
# https://stackoverflow.com/questions/2328235/pythonextend-the-dict-class
class Operators(dict):
    LEFT = True
    RIGHT = False

    def __init__(self, *args, **kw):
        super(Operators, self).__init__(*args, **kw)

    def add(name, perc, leftAssoc):
        super(Operators, self).__setitem__(name, Precedence(prec, leftAssoc))

class Expr(Element):
    def __init__(self, clazz, exp, m):
        self.factory = Factory.getForASTList(clazz)
        self.ops = m
        self.factor = exp

    def parse(self, lexer, res):
        right = self.factor.parse(lexer)
        prec = None
        while (prec = nextOperator(lexer)) != None:
            right = doShift(lexer, right, prec.value)

        res.add(right)

    def doShift(self, lexer, left, prec):
        l = list()
        l.append(left)
        l.append(ASTLeaf(lexer.read()))
        right = factor.parse(lexer)
        while (n = nextOperator(lexer)) != None and rightIsExpr(prec, n):
            right = doShift(lexer, right, n.value)
        l.append(right)
        return self.factory.make(l)

    def nextOperator(self, lexer):
        t = lexer.peek(0)
        if t.isIdentifier():
            return ops.get(t.getText())
        else:
            return None

    def rightIsExpr(self, prec, nextPrec):
        if nextPrec.leftAssoc:
            return prec < nextPrec.value
        else:
            return prec <= nextPrec.value

    def match(self, lexer):
        return self.factory.match(lexer)

class Factory():
    def make0(self):
        pass

    def make(self, arg):
        try:
            return make0(arg)
        except Exception as e:
            raise e

    def getForASTList(self, clazz):
        pass
        #f = get(clazz, list)
        #if f == None:
            #f = Factory()



class Parser():
    pass
'''
