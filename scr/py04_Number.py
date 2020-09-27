# coding=utf-8

'''
Python 数字运算
Python 解释器可以作为一个简单的计算器：您可以在解释器里输入一个表达式，它将输出表达式的值。

'''

# 表达式的语法很直白： ​+​, ​-​, ​*​ 和​/​ 和在许多其它语言（如 Pascal 或 C ）里一样；括号可以用来为运算分组。例如：
print(2 + 2)
# 4
print(50 - 5*6)
# 20
print((50 - 5*6) / 4)
# 5.0
print(8 / 5)  # 总是返回一个浮点数
# 1.6

'''
注意：在不同的机器上浮点运算的结果可能会不一样。之后我们会介绍有关控制浮点运算输出结果的内容。
在整数除法中，除法​/​总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符​ //​ ：
'''
print(17 / 3)  # 整数除法返回浮点型
# 5.666666666666667
print(17 // 3)  # 整数除法返回向下取整后的结果
# 5
print(17 % 3)  # ％操作符返回除法的余数
# 2
print(5 * 3 + 2)
# 17

# 注意：​//​是否得到整数类型的数与分母分子的数据类型有关。

print(7//2)
# 3
print(7.0//2)
# 3.0
print(7//2.0)
# 3.0

# 等号=​用于给变量赋值。赋值之后，除了下一个提示符，解释器不会显示任何结果。
# >>> width = 20
# >>> height = 5*9
# >>> width * height
# 900

# Python 可以使用​**​操作来进行幂运算：
print(5 ** 2)  # 5 的平方
# 25
print(2 ** 7)  # 2的7次方
# 128

# 变量在使用前必须先"定义"（即赋予变量一个值），否则会出现错误：
# >>> # 尝试访问一个未定义的变量
# ... n
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'n' is not defined

# 浮点数得到完全的支持；不同类型的数混合运算时会将整数转换为浮点数：
print(3 * 3.75 / 1.5)
# 7.5
print(7.0 / 2)
# 3.5

# 在交互模式中，最后被输出的表达式结果被赋值给变量 _ 。这能使您在把Python作为一个桌面计算器使用时使后续计算更方便，例如：
# >>> tax = 12.5 / 100
# >>> price = 100.50
# >>> price * tax
# 12.5625
# >>> price + _
# 113.0625
# >>> round(_, 2)
# 113.06

# 此处， _ 变量应被用户视为只读变量。不要显式地给它赋值——这样您将会创建一个具有相同名称的独立的本地变量，并且屏蔽了这个内置变量的功能。