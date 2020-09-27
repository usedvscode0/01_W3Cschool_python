# coding=utf-8

import sys         # 引入 sys 模块
'''
Python3 迭代器与生成器
迭代器
迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器：
'''

list1 = [1, 2, 3, 4]
it = iter(list1)    # 创建迭代器对象
print(next(it))    # 输出迭代器的下一个元素
print(next(it))
print(next(it))
print(next(it))

# 迭代器对象可以使用常规for语句进行遍历：
list2 = [1, 2, 3, 4]
it = iter(list2)    # 创建迭代器对象
for x in it:
    print(x, end=" ")
# 执行以上程序，输出结果如下：
# 1 2 3 4

# 也可以使用 next() 函数：
# import sys         # 引入 sys 模块

list3 = [1, 2, 3, 4]
it = iter(list3)    # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        # sys.exit()
        pass
