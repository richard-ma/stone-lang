# stone-lang
A testing project for creation of computer language

## 参考书籍
* [两周自制脚本语言](https://www.amazon.cn/dp/B0153171U2/ref=sr_1_1?s=digital-text&ie=UTF8&qid=1533199542&sr=1-1&keywords=%E4%B8%A4%E5%91%A8%E8%87%AA%E5%88%B6%E8%84%9A%E6%9C%AC%E8%AF%AD%E8%A8%80)

## Stone语法

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

## 词法分析
* 将程序分解为Token（单词或者操作符），存入StoneToken对象中
* 使用正则表达式进行分类

### Token分类
* 标识符 `[A-Za-z][A-Za-z0-9]*|==|<=|>=|&&|\|\|` `字母开头的字母和数字,以及运算符号组成标识符`
* 数值 `[0-9]+` `纯数字为数值字面量`
* 字符串 `(\\"|\\\\|\\n|[^"])*`

## 语法分析
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

### Stone语言语法

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
