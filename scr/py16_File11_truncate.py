# coding=utf-8


'''
Python3 File truncate() 方法
Python3 File(文件) 方法 Python3 File(文件) 方法
概述
truncate() 方法用于截断文件，如果指定了可选参数 size，则表示截断文件为 size 个字符。 如果没有指定 size，则重置到当前位置。
语法
truncate() 方法语法如下：
fileObject.truncate( [ size ])
参数
size -- 可选，如果存在则文件截断为 size 字节。
返回值
该方法没有返回值。
'''

# 实例
# 以下实例演示了 truncate() 方法的使用：
# 文件 youj2.txt 的内容如下：
# 1:www.w3cschool.cn
# 2:www.w3cschool.cn
# 3:www.w3cschool.cn
# 4:www.w3cschool.cn
# 5:www.w3cschool.cn

# 循环读取文件的内容：

# 打开文件
fo = open("youj2.txt", "r+", encoding='UTF-8')
print("文件名: ", fo.name)

line = fo.readline()
print("读取行: %s" % (line))

fo.truncate()
line = fo.readlines()
print("读取行: %s" % (line))

# 关闭文件
fo.close()
