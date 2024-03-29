# coding=utf-8

import operator
'''
Python3 元组
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
'''

# 如下实例：
tup1 = ('Google', 'W3CSchool', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
tup4 = (1, 2, 3, 4, 5, 5, 5, 5)

print(tup1)
print(tup2)
print(tup3)
print(tup4)

# 创建空元组
tup5 = ()
print(tup5)

# 元组中只包含一个元素时，需要在元素后面添加逗号
tup6 = (50,)
print(tup6)
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合等。

# 访问元组
# 元组可以使用下标索引来访问元组中的值，如下实例:
tup7 = ('Google', 'W3CSchool', 1997, 2000)
tup8 = (1, 2, 3, 4, 5, 6, 7)
print("tup7[0]: ", tup1[0])
print("tup8[1:5]: ", tup2[1:5])
# 以上实例输出结果：
# tup1[0]:  Google
# tup2[1:5]:  (2, 3, 4, 5)

# 修改元组
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
tup9 = (12, 34.56)
tup10 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup9[0] = 100

# 创建一个新的元组
tup11 = tup9 + tup10
print(tup11)
# 以上实例输出结果：
# (12, 34.56, 'abc', 'xyz')

# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
tup11 = ('Google', 'W3CSchool', 1997, 2000)

print(tup11)
del tup11
try:
    print("删除后的元组 tup11 : ")
    print(tup11)
except NameError:
    pass
finally:
    print("削除したので、NameError: name 'tup' is not definedをキャッチする")

# 以上实例元组被删除后，输出变量会有异常信息，输出如下所示：
# 删除后的元组 tup :
# Traceback (most recent call last):
#   File "test.py", line 8, in <module>
#     print (tup)
# NameError: name 'tup' is not defined

# 元组运算符
# 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
# Python 表达式	结果	描述
# len((1, 2, 3))	3	计算元素个数
# (1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	复制
# 3 in (1, 2, 3)	True	元素是否存在
# for x in (1, 2, 3): print x,	1 2 3	迭代

# 元组索引，截取
# 因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素，如下所示：
# 元组：
# L = ('Google', 'Taobao', 'W3CSchool')
# Python 表达式	结果	描述
# L[2]	'W3CSchool!'	读取第三个元素
# L[-2]	'Taobao'	反向读取；读取倒数第二个元素
# L[1:]	('Taobao', 'W3CSchool!')	截取元素，从第二个开始后的所有元素。

# 运行实例如下：
# >>> L = ('Google', 'Taobao', 'W3CSchool')
# >>> L[2]
# 'W3CSchool'
# >>> L[-2]
# 'Taobao'
# >>> L[1:]
# ('Taobao', 'W3CSchool')

# 元组内置函数
# Python元组包含了以下内置函数
# len(tuple)    计算元组元素个数。
tuple12 = ('Google', 'W3CSchool', 'Taobao')
print(len(tuple12))

# max(tuple)    返回元组中元素最大值。
tuple13 = ('5', '4', '8')
print(max(tuple13))

# min(tuple)    返回元组中元素最小值。
tuple14 = ('5', '4', '8')
print(min(tuple14))

# tuple(seq)    将列表转换为元组。
list15 = ['Google', 'Taobao', 'W3CSchool', 'Baidu']
tuple15 = tuple(list15)
print(tuple15)

# cmp(tuple1,tuple2)    较两个元组元素
tuple16 = (123, 'xyz')
tuple17 = (456, 'abc')
# print(cmp(tuple16, tuple17))
# Python 3.X 的版本中已经没有 cmp 函数，如果你需要实现比较功能，需要引入 operator 模块，适合任何对象，包含的方法有：
# operator.lt(a, b)
# operator.le(a, b)
# operator.eq(a, b)
# operator.ne(a, b)
# operator.ge(a, b)
# operator.gt(a, b)
# operator.__lt__(a, b)
# operator.__le__(a, b)
# operator.__eq__(a, b)
# operator.__ne__(a, b)
# operator.__ge__(a, b)
# operator.__gt__(a, b)
print(operator.eq('hello', 'name'))
print(operator.eq('hello', 'hello'))
