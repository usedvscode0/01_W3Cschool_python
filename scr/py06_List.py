# coding=utf-8

'''
Python 列表
Python囊括了大量的复合数据类型，用于组织其它数值。最有用的是列表，即写在方括号之间、用逗号分隔开的数值列表。列表内的项目不必全是相同的类型。
'''
list1 = ['Google', 'W3Cschool', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
# list1[0]:  Google
# list2[1:5]:  [2, 3, 4, 5]

# 像字符串一样，列表可以被索引和切片：
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])    # 索引返回的指定项
print(squares[-1])
print(squares[-3:])    # 切割列表并返回新的列表

# 所有的分切操作返回一个包含有所需元素的新列表。如下例中，分切将返回列表 squares 的一个拷贝：
squares2 = squares[:]
print(id(squares) == id(squares2))
print(squares2)

# 文字列はidが同じになってるけど、Listのidが違う
aaaa = '123456'
bbbb = aaaa[:]
print(id(aaaa))
print(id(bbbb))
print(id(aaaa) == id(bbbb))

# 列表还支持拼接操作：
print(squares + [36, 49, 64, 81, 100])

# Python 字符串是固定的，列表可以改变其中的元素：
cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 64    # 修改列表值
print(cubes)

# 您也可以通过使用append()方法在列表的末尾添加新项：
cubes.append(216)    # cube列表中添加新值
print(cubes)
cubes.append(7)    # cube列表中添加第七个值

# 你也可以修改指定区间的列表值：
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 替换一些值
letters[2:5] = ['C', 'D', 'E']
print(letters)
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# 移除值
letters[2:5] = []
print(letters)
# ['a', 'b', 'f', 'g']

# 清除列表
letters[:] = []
print(letters)
# []

# 内置函数 len() 用于统计列表：
letters = ['a', 'b', 'c', 'd']
print(len(letters))
# 4

# 也可以使用嵌套列表（在列表里创建其它列表），例如：
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
# [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])
# ['a', 'b', 'c']
print(x[0][1])
# 'b'
