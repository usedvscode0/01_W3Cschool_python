# coding=utf-8

'''
Python 字符串
除了数字，Python也能操作字符串。字符串有几种表达方式，可以使用单引号或双引号括起来：
'''
print('spam eggs')
# 'spam eggs'
print('doesn\'t')
# "doesn't"
print("doesn't")
# "doesn't"
print('"Yes," he said.')
# '"Yes," he said.'
print("\"Yes,\" he said.")
# '"Yes," he said.'
print('"Isn\'t," she said.')
# '"Isn\'t," she said.'

'''
Python中使用反斜杠转义引号和其它特殊字符来准确地表示。
如果字符串包含有单引号但不含双引号，则字符串会用双引号括起来，否则用单引号括起来。对于这样的输入字符串，print() 函数会产生更易读的输出。
跨行的字面字符串可用以下几种方法表示。使用续行符，即在每行最后一个字符后使用反斜线来说明下一行是上一行逻辑上的延续：
以下使用 \n 来添加新行：
'''
# >>> '"Isn\'t," she said.'
# '"Isn\'t," she said.'
# >>> print('"Isn\'t," she said.')
# "Isn't," she said.
# >>> s = 'First line.\nSecond line.'  # \n 意味着新行
# >>> s  # 不使用 print(), \n 包含在输出中
# 'First line.\nSecond line.'
# >>> print(s)  # 使用 print(), \n 输出一个新行
# First line.
# Second line.

# 以下使用 反斜线（\） 来续行：
hello = "This is a rather long string containing\n\
several lines of text just as you would do in C.\n\
    Note that whitespace at the beginning of the line is\
 significant."

print(hello)
'''
注意，其中的换行符仍然要使用 \n 表示——反斜杠后的换行符被丢弃了。以上例子将如下输出：
This is a rather long string containing
several lines of text just as you would do in C.
    Note that whitespace at the beginning of the line is significant.
'''

# 或者，字符串可以被 """ （三个双引号）或者 '''（三个单引号）括起来。
# 使用三引号时，换行符不需要转义，它们会包含在字符串中。以下的例子使用了一个转义符，避免在最开始产生一个不需要的空行。
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
'''
其输出如下：
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
'''

# 如果我们使用"原始"字符串，那么 \n 不会被转换成换行，行末的的反斜杠，以及源码中的换行符，都将作为数据包含在字符串内。例如：
hello = r"This is a rather long string containing\n\
several lines of text much as you would do in C."

print(hello)
'''
将会输出：
This is a rather long string containing\n\
several lines of text much as you would do in C.
'''

# 字符串可以使用 + 运算符串连接在一起，或者用 * 运算符重复：
word = 'Help' + 'A'
print(word)
print('<' + word*5 + '>')

# 两个紧邻的字面字符串将自动被串连；上例的第一行也可以写成 word = 'Help' 'A' ；这样的操作只在两个字面值间有效，不能随意用于字符串表达式中：
# >>> 'str' 'ing'                   #  <- string="">>> 'str'.strip() + 'ing'   #  <- string="">>> 'str'.strip() 'ing'     #  <-  这样操作错误   File "", line 1, in ?
#     'str'.strip() 'ing'
#                       ^
# SyntaxError: invalid syntax

# 字符串可以被索引；就像 C 语言一样，字符串的第一个字符的索引为 0。没有单独的字符类型；一个字符就是长度为一的字符串。就像Icon编程语言一样，子字符串可以使用分切符来指定：用冒号分隔的两个索引。
print(word)
print(word[4])
print(word[0:2])
print(word[2:4])

# 默认的分切索引很有用：默认的第一个索引为零，第二个索引默认为字符串可以被分切的长度。
print(word[0:2])    # 前两个字符
print(word[2:])     # 除了前两个字符之外，其后的所有字符

# 不同于C字符串的是，Python字符串不能被改变。向一个索引位置赋值会导致错误：
try:
    word[0] = 'x'
except TypeError:
    pass
finally:
    print(r"word[0] = 'x'がTypeErrorになる")

# 然而，用组合内容的方法来创建新的字符串是简单高效的：
print('x' + word[1:])
print('Splat' + word[4])
# 在分切操作字符串时，有一个很有用的规律： s[:i] + s[i:] 等于 s
print(word)
print(word[:2] + word[2:])
print(word[:3] + word[3:])

# 对于有偏差的分切索引的处理方式也很优雅：一个过大的索引将被字符串的大小取代，上限值小于下限值将返回一个空字符串。
print(word[1:100])
print(word[10:])
print(word[2:1])

# 在索引中可以使用负数，这将会从右往左计数。例如：
print(word[-1])    # 最后一个字符
# 'A'
print(word[-2])     # 倒数第二个字符
# 'p'
print(word[-2:])   # 最后两个字符
# 'pA'
print(word[:-2])   # 除了最后两个字符之外，其前面的所有字符
# 'Hel'
# 但要注意， -0 和 0 完全一样，所以 -0 不会从右开始计数！
print(word[-0])    # (既然 -0 等于 0)
# 'H'

# 超出范围的负数索引会被截去多余部分，但不要尝试在一个单元素索引（非分切索引）里使用：
print(word[-100:])
try:
    print(word[100])
except IndexError:
    pass
finally:
    print("print(word[100])にIndexErrorが発生された")

# 有一个方法可以让您记住分切索引的工作方式，想像索引是指向字符之间，第一个字符左边的数字是 0。接着，有n个字符的字符串最后一个字符的右边是索引n，例如：
#  +---+---+---+---+---+
#  | H | e | l | p | A |
#  +---+---+---+---+---+
#  0   1   2   3   4   5
# -5  -4  -3  -2  -1

# 第一行的数字 0...5 给出了字符串中索引的位置；第二行给出了相应的负数索引。分切部分从 i 到 j 分别由在边缘被标记为 i 和 j 的全部字符组成。
# 对于非负数分切部分，如果索引都在有效范围内，分切部分的长度就是索引的差值。例如， word[1:3] 的长度是2。
# 内置的函数 len() 用于返回一个字符串的长度：
s = 'supercalifragilisticexpialidocious'
print(len(s))
x = '第一行'
print(len(x))
