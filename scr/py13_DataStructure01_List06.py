# coding=utf-8

'''
del 语句
使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。
例如：
'''
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
# [1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)
# [1, 66.25, 1234.5]
del a[:]
print(a)

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a
try:
    print(a)
except NameError:
    pass
finally:
    print('NameError: is catched')
