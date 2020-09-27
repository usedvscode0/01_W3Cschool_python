# coding=utf-8

'''
Python 模块
在前面的几个章节中我们脚本上是用python解释器来编程，如果你从Python解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用python标准库的方法。下面是一个使用python标准库中模块的例子。
'''
import sys

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')

# 1、import sys引入python标准库中的sys.py模块；这是引入某一模块的方法。
# 2、sys.argv是一个包含命令行参数的列表。
# 3、sys.path包含了一个Python解释器自动查找所需模块的路径的列表。
