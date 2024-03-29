# coding=utf-8

'''
Python运算符优先级
以下表格列出了从最高到最低优先级的所有运算符：

运算符	描述
**	指数 (最高优先级)
~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	乘，除，取模和取整除
+ -	加法减法
>> <<	右移，左移运算符
&	位 'AND'
^ |	位运算符
<= < > >=	比较运算符
<> == !=	等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	身份运算符
in not in	成员运算符
not or and	逻辑运算符
'''

# 以下实例演示了Python所有运算符优先级的操作：
a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：",  e)

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：",  e)

e = (a + b) * (c / d)    # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：",  e)

e = a + (b * c) / d      # 20 + (150/5)
print("a + (b * c) / d 运算结果为：",  e)

'''
以上实例输出结果：

(a + b) * c / d 运算结果为： 90.0
((a + b) * c) / d 运算结果为： 90.0
(a + b) * (c / d) 运算结果为： 90.0
a + (b * c) / d 运算结果为： 50.0
'''
