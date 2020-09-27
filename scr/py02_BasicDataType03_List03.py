# coding=utf-8

# 与Python字符串不一样的是，列表中的元素是可以改变的：

a = [1, 2, 3, 4, 5, 6]
a[0] = 9
print(a)
a[2:5] = [13, 14, 15, 16, 16, 16, 16, 16]
print(a)

a[2:5] = []   # 删除
print(a)

# append()
# pop()

a.append(20)
print(a)
a.append([30, 30])
print(a)
a.pop(1)
print(a)

'''
List内置了有很多方法，例如append()、pop()等等，这在后面会讲到。
注意：
1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。
'''
