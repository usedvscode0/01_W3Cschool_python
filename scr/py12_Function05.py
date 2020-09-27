# coding=utf-8

# 返回值
# Python的函数的返回值使用return语句，可以将函数作为一个值赋值给指定变量：
def return_sum(x, y):
    c = x + y
    return c


res1 = return_sum(4, 5)
print(res1)


# 你也可以让函数返回空值：
def empty_return(x, y):
    c = x + y
    return


# res1 = return_sum(4, 5)
print(empty_return(4, 5))
