# coding=utf-8
# Filename: py14_Module03__name_.py

import py14_Module00_using_name

'''
__name__属性
一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，
我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
'''

if __name__ == '__main__':
    print('程序自身在运行')
    print(__name__)
else:
    print('我来自另一模块')
    print(__name__)

py14_Module00_using_name.test()
'''
运行输出如下：

$ python using_name.py
程序自身在运行
$ python
>>> import using_name
我来自另一模块
>>>
说明：

每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
__name__ 与 __main__ 底下是双下划线，是“_ _”去掉中间的空格。
'''
