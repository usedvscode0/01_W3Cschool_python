# coding=utf-8

'''
Python3 File 方法
Python3 File(文件) 方法
file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：
序号	方法及描述
1
file.close()
关闭文件。关闭后文件不能再进行读写操作。
2
file.flush()
刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
3
file.fileno()
返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
4
file.isatty()
如果文件连接到一个终端设备返回 True，否则返回 False。
5
file.next()
返回文件下一行。
6
file.read([size])
从文件读取指定的字节数，如果未给定或为负则读取所有。
7
file.readline([size])
读取整行，包括 "\n" 字符。
8
file.readlines([sizehint])
读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比sizeint较大, 因为需要填充缓冲区。
9
file.seek(offset[, whence])
设置文件当前位置
10
file.tell()
返回文件当前位置。
11
file.truncate([size])
截取文件，截取的字节通过size指定，默认为当前文件位置。
12
file.write(str)
将字符串写入文件，返回的是写入的字符长度。
13
file.writelines(sequence)
向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
'''

'''
Python3 File close() 方法
Python3 File(文件) 方法 Python3 File(文件) 方法
概述
close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。 close() 方法允许调用多次。
当 file 对象，被引用到操作另外一个文件时，Python 会自动关闭之前的 file 对象。 使用 close() 方法关闭文件是一个好的习惯。
语法
close() 方法语法如下：
fileObject.close();
参数
无
返回值
该方法没有返回值。
'''

# 实例
# 以下实例演示了 close() 方法的使用：

# 打开文件
fo = open("youj.txt", "wb")
print("文件名为: ", fo.name)

# 关闭文件
fo.close()

# 以上实例输出结果为：
# 文件名为:  youj.txt
