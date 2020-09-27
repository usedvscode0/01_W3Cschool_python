# coding=utf-8
'''
字典（dictionary）是Python中另一个非常有用的内置数据类型。
字典是一种映射类型（mapping type），它是一个无序的键 : 值对集合。
关键字必须使用不可变类型，也就是说list和包含可变类型的tuple不能做关键字。
在同一个字典中，关键字还必须互不相同。
'''

dic = {}  # 创建空字典
tel = {'Jack': 1557, 'Tom': 1320, 'Rose': 1886}
print(tel)

print(tel['Jack'])   # 主要的操作：通过key查询

del tel['Rose']  # 删除一个键值对
print(tel)

tel['Mary'] = 4127  # 添加一个键值对
print(tel)

print(list(tel.keys()))  # 返回所有key组成的list

print(sorted(tel.keys()))  # 按key排序

print('Tom' in tel)       # 成员测试
print('Mary' not in tel)  # 成员测试
