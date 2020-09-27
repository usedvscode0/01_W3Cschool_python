# coding=utf-8


'''
Python3 File readlines() 方法
Python3 File(文件) 方法 Python3 File(文件) 方法
概述
readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比sizhint较大, 因为需要填充缓冲区。
如果碰到结束符 EOF 则返回空字符串。
语法
readlines() 方法语法如下：
fileObject.readlines( sizehint );
参数
sizehint -- 从文件中读取的字节数。
返回值
返回列表，包含所有的行。
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

line = fo.readlines(2)
print("读取的数据为: %s" % (line))

line = fo.readlines(4)
print("读取的数据为: %s" % (line))

line = fo.readlines()
print("读取的数据为: %s" % (line))

# 关闭文件
fo.close()
