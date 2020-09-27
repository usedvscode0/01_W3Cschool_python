# coding=utf-8

'''
Python 条件控制
if 语句
Python中if语句的一般形式如下所示：
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句，如果 "condition_1" 为False，将判断 "condition_2"，如果"condition_2" 为 True 将执行 "statement_block_2" 块语句，如果 "condition_2" 为False，将执行"statement_block_3"块语句。
Python中用elif代替了else if，所以if语句的关键字为：if – elif – else。
注意：
1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在Python中没有switch – case语句。
'''

# 实例
# 以下实例演示了狗的年龄计算判断：
age = int(input("Age of the dog: "))
print()
if age < 0:
    print("This can hardly be true!")
elif age == 1:
    print("about 14 human years")
elif age == 2:
    print("about 22 human years")
elif age > 2:
    human = 22 + (age - 2)*5
    print("Human years: ", human)
###
input('press Return>')

# 将以上脚本保存在dog.py文件中，并执行该脚本：
# python dog.py
# Age of the dog: 1
# about 14 human years

# 以下为if中常用的操作运算符:
# 操作符	描述
# <	小于
# <=	小于或等于
# >	大于
# >=	大于或等于
# ==	等于，比较对象是否相等
# !=	不等于

# 实例
# 程序演示了 == 操作符
# 使用数字
print(5 == 6)
# 使用变量
x = 5
y = 8
print(x == y)
# 以上实例输出结果：
# False
# False

# high_low.py文件：
# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("Guess the number!")
while guess != number:
    guess = int(input("Is it... "))

    if guess == number:
        print("Hooray! You guessed it right!")
    elif guess < number:
        print("It's bigger...")
    elif guess > number:
        print("It's not so big.")
