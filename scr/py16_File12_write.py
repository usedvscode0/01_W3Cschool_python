# coding=utf-8


'''
Python3 File write() 方法
Python3 File(文件) 方法 Python3 File(文件) 方法
概述
write() 方法用于向文件中写入指定字符串。
在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。
语法
write() 方法语法如下：
fileObject.write( [ str ])
参数
str -- 要写入文件的字符串。
返回值
该方法没有返回值。
'''

# 实例
# 以下实例演示了 write() 方法的使用：
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

str = "6:www.w3cschool.cn"
# 在文件末尾写入一行
fo.seek(0, 2)
line = fo.write(str)

# 读取文件所有内容
fo.seek(0, 0)
for index in range(6):
    line = next(fo)
    print("文件行号 %d - %s" % (index, line))

# 关闭文件
fo.close()
