# coding=utf-8

'''
import语句
如果要使用Python源文件，只需在另一个源文件里执行import语句，import语句语法如下：
import module1[,module2[, ... moduleN]
当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
搜索路径是一个解释器会先进行搜索的所有目录的列表。如果想要导入模块 support，需要把命令放在脚本的顶端：
'''


def print_func(par):
    print("Hello : ", par)
    return

# print(print_func('aaa'))
