# coding=utf-8

'''
函数变量作用域
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
通过以下实例，你可以清楚了解Python函数变量的作用域：
'''

a = 4  # 全局变量


def print_func1():
    a = 17    # 局部变量
    print("in print_func a = ", a)


def print_func2():
    print("in print_func a = ", a)


print_func1()
print_func2()
print("a = ", a)

# 以上实例运行结果如下：
# in print_func a =  17
# in print_func a =  4
# a =  4
