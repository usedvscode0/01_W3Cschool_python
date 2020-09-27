# coding=utf-8

# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对：
dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict1)
# {'sape': 4139, 'jack': 4098, 'guido': 4127}

# 此外，字典推导可以用来创建任意键和值的表达式词典：
dict2 = {x: x**2 for x in (2, 4, 6)}
print(dict2)

# 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便：
dict3 = dict(sape=4139, guido=4127, jack=4098)
# {'sape': 4139, 'jack': 4098, 'guido': 4127}
