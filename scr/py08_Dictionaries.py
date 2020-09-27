# coding=utf-8

'''
Python3 字典
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
d = {key1 : value1, key2 : value2 }
'''

# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
# 一个简单的字典实例：
dict0 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# 也可如此创建字典
dict1 = {'abc': 456}
dict2 = {'abc': 123, 98.6: 37}

# 访问字典里的值
# 把相应的键放入熟悉的方括弧，如下实例:
dict3 = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}
print("dict3['Name']: ", dict3['Name'])
print("dict3['Age']: ", dict3['Age'])
# 以上实例输出结果：
# dict3['Name']:  W3CSchool
# dict3['Age']:  7

# 如果用字典里没有的键访问数据，会输出错误如下：
try:
    dict4 = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}
    print("dict['Alice']: ", dict4['Alice'])
except KeyError:
    pass
else:
    pass
finally:
    print('KeyError catched')
# 以上实例输出结果：
# Traceback (most recent call last):
#   File "test.py", line 5, in <module>
#     print ("dict['Alice']: ", dict['Alice'])
# KeyError: 'Alice'

# 修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
dict5 = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}
dict5['Age'] = 8    # 更新 Age
dict5['School'] = "W3Cschool教程"    # 添加信息
print("dict5['Age']: ", dict5['Age'])
print("dict5['School']: ", dict5['School'])
# 以上实例输出结果：
# dict5['Age']:  8
# dict5['School']:  W3Cschool教程

# 删除字典元素
# 能删单一的元素也能清空字典，清空只需一项操作。
# 显示删除一个字典用del命令，如下实例：
dict6 = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}
del dict6['Name']    # 删除键 'Name'
dict6.clear()    # 删除字典
del dict6    # 删除字典
try:
    print("dict6['Age']: ", dict6['Age'])

except NameError:
    pass
finally:
    print("dict6['Age']: is TypeError was catched")

try:
    print("dict6['School']: ", dict6['School'])
except NameError:
    pass
finally:
    print("dict6['School']: is TypeError was catched")
# 但这会引发一个异常，因为用执行 del 操作后字典不再存在：
# Traceback (most recent call last):
#   File "test.py", line 9, in <module>
#     print ("dict['Age']: ", dict['Age'])
# TypeError: 'type' object is not subscriptable
# 注：del() 方法后面也会讨论。


# 字典键的特性
# 字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：

# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
dict7 = {'Name': 'W3CSchool', 'Age': 7, 'Name': '小菜鸟'}
print("dict['Name']: ", dict7['Name'])

# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
try:
    dict7 = {['Name']: 'W3CSchool', 'Age': 7}
    print("dict7['Name']: ", dict7['Name'])
except TypeError:
    pass
finally:
    print("dict7['Name']: is TypeError catched")
# Traceback (most recent call last):
#   File "test.py", line 3, in <module>
#     dict = {['Name']: 'W3CSchool', 'Age': 7}
# TypeError: unhashable type: 'list'

# 字典内置函数&方法
# Python字典包含了以下内置函数：
# len(dict)    计算字典元素个数，即键的总数。
dict8 = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}
print(len(dict8))

# str(dict)    输出字典以可打印的字符串表示。
dict9 = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}
print(str(dict9))

# type(variable)    返回输入的变量类型，如果变量是字典就返回字典类型。
dict10 = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}
print(type(dict10))

# Python字典包含了以下内置方法：
# 序号	函数及描述
# 1	radiansdict.clear()
# 删除字典内所有元素
# 2	radiansdict.copy()
# 返回一个字典的浅复制
# 3	radiansdict.fromkeys()
# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# f4	radiansdict.get(key, default=None)
# 返回指定键的值，如果值不在字典中返回default值
# 5	key in dict
# 如果键在字典dict里返回true，否则返回false
# 6	radiansdict.items()
# 以列表返回可遍历的(键, 值) 元组数组
# 7	radiansdict.keys()
# 以列表返回一个字典所有的键
# 8	radiansdict.setdefault(key, default=None)
# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# 9	radiansdict.update(dict2)
# 把字典dict2的键/值对更新到dict里
# 10	radiansdict.values()
# 以列表返回字典中的所有值

'''
Python3 字典 clear()方法
描述:Python 字典 clear() 函数用于删除字典内所有元素。
语法:clear()方法语法：dict.clear()
参数:NA。
返回值:该函数没有任何返回值。
实例
以下实例展示了 clear()函数的使用方法：
'''
dict11 = {'Name': 'Zara', 'Age': 7}
print("字典长度 : %d" % len(dict11))
dict11.clear()
print("字典删除后长度 : %d" % len(dict11))
# 以上实例输出结果为：
# 字典长度 : 2
# 字典删除后长度 : 0

'''
Python3 字典 copy()方法
描述:Python 字典 copy() 函数返回一个字典的浅复制。
语法:copy()方法语法：dict.copy()
参数:NA。
返回值:返回一个字典的浅复制。
实例
以下实例展示了 copy()函数的使用方法：
'''
dict12 = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}
dict13 = dict12.copy()
print("新复制的字典为 : ", dict13)
print(id(dict12) == id(dict13))
# 以上实例输出结果为：
# 新复制的字典为 :  {'Age': 7, 'Name': 'W3CSchool', 'Class': 'First'}

'''
Python3 字典 fromkeys()方法
描述:Python 字典 fromkeys() 函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
语法:fromkeys()方法语法：dict.fromkeys(seq[, value]))
参数:
seq -- 字典键值列表。
value -- 可选参数, 设置键序列（seq）的值。
返回值:该方法返回列表。
实例
以下实例展示了 fromkeys()函数的使用方法：
'''
seq14 = ('name', 'age', 'sex')
dict14 = dict.fromkeys(seq14)
print("新的字典为 : %s" % str(dict14))
dict15 = dict.fromkeys(seq14, 10)
print("新的字典为 : %s" % str(dict15))
# 以上实例输出结果为：
# 新的字典为 : {'age': None, 'name': None, 'sex': None}
# 新的字典为 : {'age': 10, 'name': 10, 'sex': 10}

'''
Python3 字典 get() 方法
描述:Python 字典 get() 函数返回指定键的值，如果值不在字典中返回默认值。
语法:get()方法语法：dict.get(key, default=None)
参数:
key -- 字典中要查找的键。
default -- 如果指定键的值不存在时，返回该默认值值。
返回值:返回指定键的值，如果值不在字典中返回默认值 None。
实例
以下实例展示了 get()函数的使用方法：
'''
dict16 = {'Name': 'W3CSchool', 'Age': 27}
print("Age 值为 : %s" % dict16.get('Age'))
print("Sex 值为 : %s" % dict16.get('Sex', "NA"))
print("Sex 值为 : %s" % dict16.get('Sex'))
# 以上实例输出结果为：
# Age 值为 : 27
# Sex 值为 : NA

'''
Python3 字典 in 操作符
描述:Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典dict里返回true，否则返回false。
语法:has_key()方法语法：key in dict
参数:
key -- 要在字典中查找的键。
返回值:如果键在字典里返回true，否则返回false。
实例
以下实例展示了 in 操作符在字典中的使用方法：
'''
dict17 = {'Name': 'W3CSchool', 'Age': 7}
# 检测键 Age 是否存在
if 'Age' in dict17:
    print("键 Age 存在")
else:
    print("键 Age 不存在")

# 检测键 Sex 是否存在
if 'Sex' in dict17:
    print("键 Sex 存在")
else:
    print("键 Sex 不存在")
# 以上实例输出结果为：
# 键 Age 存在
# 键 Sex 不存在

'''
Python3 字典 items() 方法
描述:Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
语法:items()方法语法：dict.items()
参数:NA。
返回值:返回可遍历的(键, 值) 元组数组。
实例
以下实例展示了 items() 方法的使用方法：
'''
dict18 = {'Name': 'W3CSchool', 'Age': 7}
print("Value : %s" % dict18.items())
# 以上实例输出结果为：
# Value : dict_items([('Age', 7), ('Name', 'W3CSchool')])

'''
Python3 字典 keys() 方法
描述:Python 字典 keys() 方法以列表返回一个字典所有的键。
语法:keys()方法语法：dict.keys()
参数:NA。
返回值:返回一个字典所有的键。
实例
以下实例展示了 keys() 方法的使用方法：
'''
dict19 = {'Name': 'W3CSchool', 'Age': 7}
print("字典所有的键为 : %s" % dict19.keys())
# 以上实例输出结果为：
# 字典所有的键为 : dict_keys(['Age', 'Name'])

'''
Python3 字典 setdefault() 方法
描述:Python 字典 setdefault() 方法和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。
语法:setdefault()方法语法：dict.setdefault(key, default=None)
参数:
key -- 查找的键值。
default -- 键不存在时，设置的默认键值。
返回值:该方法没有任何返回值。
实例
以下实例展示了 setdefault() 方法的使用方法：
'''
dict20 = {'Name': 'W3CSchool', 'Age': 7}
print("Age 键的值为 : %s" % dict20.setdefault('Age', None))
print("Sex 键的值为 : %s" % dict20.setdefault('Sex', None))
print("新字典为：", dict20)
# Age 键的值为 : 7
# Sex 键的值为 : None
# 新字典为： {'Age': 7, 'Name': 'W3CSchool', 'Sex': None}

'''
Python3 字典 update() 方法
描述:Python 字典 update() 函数把字典dict2的键/值对更新到dict里。
语法:update()方法语法：dict.update(dict2)
参数:dict2 -- 添加到指定字典dict里的字典。
返回值:该方法没有任何返回值。
实例
以下实例展示了 update()函数的使用方法：
'''
dict20 = {'Name': 'W3CSchool', 'Age': 7}
dict21 = {'Sex': 'female'}
dict20.update(dict21)
print("更新字典 dict20 : ", dict20)
# 更新字典 dict :  {'Sex': 'female', 'Age': 7, 'Name': 'W3CSchool'}

'''
Python3 字典 values() 方法
描述:Python 字典 values() 方法以列表返回字典中的所有值。
语法:values()方法语法：dict.values()
参数:NA。
返回值:该方法没有任何返回值。
实例
以下实例展示了 values() 方法的使用方法：
'''
dict22 = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print("字典所有值为 : ",  list(dict22.values()))
# 字典所有值为 :  ['female', 'Zara', 7]
