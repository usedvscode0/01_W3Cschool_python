# coding=utf-8


'''
Python3 File read() 方法
Python3 File(文件) 方法 Python3 File(文件) 方法
概述
read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
语法
read() 方法语法如下：
fileObject.read();
参数
size -- 从文件中读取的字节数。
返回值
返回从字符串中读取的字节。
'''

# 实例
# 以下实例演示了 read() 方法的使用：
# 文件 youj.txt 的内容如下：
# 这是第一行
# 这是第二行
# 这是第三行
# 这是第四行
# 这是第五行

# 循环读取文件的内容：

# 打开文件
fo = open("youj.txt", "r+", encoding='UTF-8')
print("文件名为: ", fo.name)

line = fo.read(10)
print("读取的字符串: %s" % (line))

# 关闭文件
fo.close()
