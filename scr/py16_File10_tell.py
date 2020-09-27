# coding=utf-8


'''
Python3 File tell() 方法
Python3 File(文件) 方法 Python3 File(文件) 方法
概述
tell() 方法返回文件的当前位置，即文件指针当前位置。
语法
tell() 方法语法如下：
fileObject.tell(offset[, whence])
参数
无
返回值
返回文件的当前位置。
'''

# 实例
# 以下实例演示了 tell() 方法的使用：
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
print("读取的数据为: %s" % (line))

# 获取当前文件位置
pos = fo.tell()
print("当前位置: %d" % (pos))

line = fo.readline()
print("读取的数据为: %s" % (line))

# 获取当前文件位置
pos = fo.tell()
print("当前位置: %d" % (pos))

# 关闭文件
fo.close()
