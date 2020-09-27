# coding=utf-8


'''
Python3 File readline() 方法
Python3 File(文件) 方法 Python3 File(文件) 方法
概述
readline() 方法用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。
语法
readline() 方法语法如下：
fileObject.readline();
参数
size -- 从文件中读取的字节数。
返回值
返回从字符串中读取的字节。
'''

# 实例
# 以下实例演示了 readline() 方法的使用：
# 文件 youj2.txt 的内容如下：
# 1:www.w3cschool.cn
# 2:www.w3cschool.cn
# 3:www.w3cschool.cn
# 4:www.w3cschool.cn
# 5:www.w3cschool.cn

# 循环读取文件的内容：

# 打开文件
fo = open("youj2.txt", "r+", encoding='UTF-8')
print("文件名为: ", fo.name)

line = fo.readline()
print("读取第一行 %s" % (line))

line = fo.readline(5)
print("读取的字符串为: %s" % (line))

# 关闭文件
fo.close()
