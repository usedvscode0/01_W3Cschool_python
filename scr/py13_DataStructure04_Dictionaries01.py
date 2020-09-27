# coding=utf-8

'''
字典
另一个非常有用的 Python 内建数据类型是字典。
序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
一对大括号创建一个空的字典：{}。
这是一个字典运用的简单例子：
'''
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
# {'sape': 4139, 'guido': 4127, 'jack': 4098}
print(tel['jack'])
# 4098
del tel['sape']
tel['irv'] = 4127
print(tel)
# {'guido': 4127, 'irv': 4127, 'jack': 4098}
print(list(tel.keys()))
# ['irv', 'guido', 'jack']
print(sorted(tel.keys()))
# ['guido', 'irv', 'jack']
print('guido' in tel)
# True
print('jack' not in tel)
# False
