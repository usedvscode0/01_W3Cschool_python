# coding=utf-8

'''
概述
isatty() 方法检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False。
语法
isatty() 方法语法如下：
fileObject.isatty();
参数
无
返回值
如果连接到一个终端设备返回 True，否则返回 False。
'''

# 实例
# 以下实例演示了 isatty() 方法的使用：
# 打开文件
fo = open("youj.txt", "wb")
print("文件名为: ", fo.name)
ret = fo.isatty()
print("返回值 : ", ret)
# 关闭文件
fo.close()
