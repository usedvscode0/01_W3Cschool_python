# coding=utf-8

# 构造函数 dict() 直接从键值对sequence中构建字典，当然也可以进行推导，如下：

dic1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dic1)

dic2 = {x: x**2 for x in (2, 4, 6)}
print(dic2)

dic3 = dict(sape=4139, guido=4127, jack=4098)
print(dic3)
print(dic3.keys())
print(dic3.values())
dic3.clear()
print(dic3)
'''
另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。
注意：
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用{ }。
'''
