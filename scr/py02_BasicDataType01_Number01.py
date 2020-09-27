# coding=utf-8

'''
Python中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在Python中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
Python 3中有六个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionaries（字典）
'''

'''
Numbers（数字）
Python 3支持int、float、bool、complex（复数）。
数值类型的赋值和计算都是很直观的，就像大多数语言一样。内置的type()函数可以用来查询变量所指的对象类型。
'''
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
