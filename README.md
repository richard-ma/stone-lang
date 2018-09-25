[![Build Status](https://www.travis-ci.org/richard-ma/stone-lang.svg?branch=master)](https://www.travis-ci.org/richard-ma/stone-lang)
[![Coverage Status](https://coveralls.io/repos/github/richard-ma/stone-lang/badge.svg)](https://coveralls.io/github/richard-ma/stone-lang)

# stone-lang
A testing project for creation of computer language

## 参考书籍
* [两周自制脚本语言](https://www.amazon.cn/dp/B0153171U2/ref=sr_1_1?s=digital-text&ie=UTF8&qid=1533199542&sr=1-1&keywords=%E4%B8%A4%E5%91%A8%E8%87%AA%E5%88%B6%E8%84%9A%E6%9C%AC%E8%AF%AD%E8%A8%80)

## 备注
* 章节名称后面括号数字对应书中章节编号

## Stone语法(2)

### 数据类型
* 数值
* 字符串

### 表达式
#### 赋值表达式
```
sum = 0
```
#### 运算表达式
```
sum = sum + 1
```
#### 条件表达式
```
i < 10
```

### 语句

#### 分支语句
```
if i % 2 == 0 {
    even = even + 1
} else {
    odd = odd + 1
}
```

#### 循环语句
```
while i < 10 {
    i = i + 1
}
```

## 词法分析(3)
* 将程序分解为Token（单词或者操作符），存入StoneToken对象中
* 使用正则表达式进行分类

### Token分类
* 标识符 `[A-Za-z][A-Za-z0-9]*|==|<=|>=|&&|\|\|` `字母开头的字母和数字,以及运算符号组成标识符`
* 数值 `[0-9]+` `纯数字为数值字面量`
* 字符串 `(\\"|\\\\|\\n|[^"])*`

## 语法分析(4)
* 将词法分析的结果构建成语法树

###  语法树
* 例如3 + 2 * 5这个表达式的语法树为
```
    2   *   5
    |   |   |
    +---+---+
        10
3   +   |
|   |   |
+---+---+
    13
```

### 语法树类设计
```
        ASTree
        |
    +---+---+
    |       |
  ASTList   ASTLeaf
    |       |
BinaryExpr  +---+
            |   | 
 NumberLiteral  Name 
```
* ASTLeaf 表示树的叶子节点
* ASTList 表示树的分支节点
* BinaryExpr 为二目操作，left()和right()方法获得操作数，operator()获得操作符
* NumberLiteral 由NumToken构建
* Name 由StrToken构建

## Stone语言语法(5)

#### BNF
`BNF`是一种语法的表示方法

* `{pat}`       pat匹配至少0次
* `[pat]`       pat匹配0次或1次
* `pat1 | pat2` 匹配pat1或pat2
* `()`          将括号内视为整体

#### 用`BNF`表示的Stone语言语法
* primary:  `"(" expr ")" | NUMBER | IDENTIFIER | STRING` (终结符)
* factor:   `"-" primary | primary` 
* expr:     `factor { OP factor }` (表达式)
* block:    `"{" [statement]{(";" | EOL) [statement]} "}"` (代码块)
* simple:   `expr` (不知道这里为什么这么写，实际上就是表达式)
* statement: (语句)
    * `"if" expr block ["else" block]` (if语句)
    * `"while" expr block` (while语句)
    * `simple` (单独的表达式)
* program:  `[statement](";" | EOL)` (整个程序)

### Parser类的方法
* `rule()/rule(Class c)` 创建Parser对象
* `parse(Lexer l)` 执行语法分析
* `number()/number(Class c)` 向语法规则中添加终结符(Number)
* `identifier(HastSet r)/identifier(Class c, HastSet r)` 向语法规则中添加除保留字r之外的标识符
* `string()/string(Class c)` 向语法规则中添加字符串终结符
* `token(String pat)` 向语法规则中添加与pat匹配的终结符
* `sep(pat)` 向语法规则中添加与pat匹配但为包含于抽象语法树的终结符
* `ast(Parser p)` 向语法规则中添加非终结符p
* `option(Parser p)` 向语法规则中添加可省略的非终结符p
* `maybe(Parser p)` 向语法规则中添加可省略的非终结符p（如果省略，则作为仅有根节点的语法树处理）
* `or(Parser p...)` 向语法规则中添加若干个具有or关系的非终结符p
* `repeat(Parser p)` 向语法规则中添加至少重复出现0次的非终结符p
* `expression(Parser p, Operators op)` 向语法规则中添加双目运算表达式（p是因子，op是运算符表）
* `reset()/reset(Class c)` 清空语法规则
* `insertChoice(Parser p)` 为语法规则起始处的or添加新的分支选项

## 语法分析方式(16)
* 使用四则运算表达式为例子进行简单的语法分析程序编写

### 四则运算BNF
* factor:       `NUMBER | "(" expression ")"` (数字或表达式)
* term :        `factor { ("*" | "/") factor }` (乘除运算)
* expression:   `term { ("+" | "-") term }` (加减运算)

### 朴素的语法分析方式
* factor、term以及expression为三个独立的函数
* 函数中使用词法分析结果判断是否符合BNF
* 使用分支语句表现或的关系
* 不能通过则抛出ParseException异常
* Code: /src/parseExpr.py
* TestCase: /samples/expression.stone
* TestCase: /samples/expression_parseexception.stone

### 包含比较和逻辑运算的表达式BNF
* factor:       `NUMBER | "(" expression ")"` (数字或表达式) [这里的expression是不是写错了？下面没有定义]
* term :        `factor { ("*" | "/") factor }` (乘除运算)
* addexpr:      `term { ("+" | "-") term }` (加减运算)
* relexpr:      `addexpr { ("<" | ">") addexpr }` (大于小于)  
* eqexpr:       `relexpr { ("==" | "!=") relexpr }` (等于不等)     
* andexpr:      `eqexpr { "&&" eqexpr }` (逻辑与)
* orexpr:       `andexpr { "||" andexpr }` (逻辑或)

### 算符优先分析法
* 将所有运算符号按照优先级登记入一个表中
* 在遇到运算符号时，按照优先级匹配
* 是LR(1)分析的简化版本
* Code: /src/opPrecedenceParser.py
* TestCase: /samples/expression.stone
* TestCase: /samples/expression_parseexception.stone

#### TIPS: Python嵌套类
```
# from /src/opPrecedenceParser.py

class A:
    class B: # 在A中的类B 一般B是只在A中使用的类
        def __init__(self, v):
            self.value = v
    def __init__(self): # 在A中使用B类的对象
        self.objOfB = self.B(5) # B类使用的时候要加上self
```

## 用于语法分析的Parser库(17)

### 组合子分析

#### 组合子类结构
```
Element-----+---Parse()
    |       +---Match()
    |
    +-------+-------+-------+-------+-------+
    |       |       |       |       |       |
 AToken    Expr    Leaf    Repeat  OrTree  Tree
    |               |             
    |              Skip
    |
    +-------+-------+
    |       |       |
 IdToken  NumToken  StrToken
```
