#!/usr/bin/env python
# encoding: utf-8

import re
from collections import deque
from stoneToken import StoneToken
from numToken import NumToken
from strToken import StrToken
from idToken import IdToken
from parseException import ParseException

class LineReader():
    def __init__(self, f):
        self.f = f
        self.lineNumber = 0

    def readline(self):
        line = self.f.readline()
        #print(line)
        if len(line) == 0: # EOF
            return None
        else:
            self.lineNumber += 1
            return line

    def getLineNumber(self): # 为了添加这个方法创建了LineReader类
        return self.lineNumber

class Lexer():
    def __init__(self, reader):
        self.regexPat = "\\s*((//.*)|([0-9]+)|(\"(\\\\\"|\\\\\\\\|\\\\n|[^\"])*\")" + \
                "|[A-Za-z][A-Za-z0-9]*|==|<=|>=|&&|\\|\\||[`~!@#\$%\^&\*\(\)-=_+\[\]\\\{\}\|;':\",./<>\?])?"
        self.pattern = re.compile(self.regexPat)
        self.queue = deque()
        self.hasMore = True
        self.reader = reader

    def read(self):
        if (self.fillQueue(0)):
            return self.queue.popleft()
        else:
            return StoneToken.EOF

    def peek(self, i):
        if (self.fillQueue(i)):
            return self.queue[i]
        else:
            return StoneToken.EOF

    def fillQueue(self, i):
        while (i >= len(self.queue)):
            if (self.hasMore):
                self.readLine()
            else:
                return False
        return True

    def readLine(self):
        try:
            line = self.reader.readline()
        except Exception as e:
            raise ParseException(e)

        if line is None: # EOF
            self.hasMore = False
            return

        lineNo = self.reader.getLineNumber() # 获得当前读取的行号
        pos = 0 # 匹配起始位置
        endPos = len(line) # 匹配结束位置
        while (pos < endPos):
            matcher = self.pattern.match(line, pos, endPos) # 在pos和endPos之间检查有无匹配
            if matcher: # 存在匹配
                self.addToken(lineNo, matcher) # 将这个匹配结果添加到token队列中 -> self.queue
                pos = matcher.end() # 更新位置，当前匹配的对象跳过去，看后面的部分
                #print("pos: %d" % (pos))
            else:
                raise ParseException("Bad token at line" + lineNo) # 没有匹配，证明这个地方的单词不合法，有语法错误
        self.queue.append(IdToken(lineNo, StoneToken.EOL)) # 添加行结束token

    def addToken(self, lineNo, matcher):
        m = matcher.group(1)
        if m is not None: # 不是空白行或空格
            if matcher.group(2) is None: # 不是注释
                if matcher.group(3) is not None:
                    token = NumToken(lineNo, int(m))
                elif matcher.group(4) is not None:
                    token = StrToken(lineNo, self.toStringLiteral(str(m)))
                else:
                    token = IdToken(lineNo, m)
                #print("[%d] %s" % (token.getLineNumber(), token.getText()))
                self.queue.append(token)

    def toStringLiteral(self, s):
        sb = list()
        l = len(s) - 1
        i = 0
        while i < l:
            c = s[i]
            if c == '\\' and i + 1 < l:
                c2 = s[i+1]
                if c2 == "" or c2 == '\\':
                    c = s[i+1]
                elif c2 == 'n':
                    i += 1
                    c = '\n'

            sb.append(c)
            i += 1
        return ''.join(sb)

if __name__ == "__main__":
    with open("../samples/first.stone", 'r') as f:
        reader = LineReader(f)
        lexer = Lexer(reader)
        token = lexer.read()
        if token != None: print(token.getText())
        while token != StoneToken.EOF:
            token = lexer.read()
            if token != None: print(token.getText())
