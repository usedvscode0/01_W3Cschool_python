# coding=utf-8

# 关键字参数
# 函数也可以使用 kwarg=value 的关键字参数形式被调用.例如,以下函数:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# 可以以下几种方式被调用:

print(parrot(1000))                                          # 1 positional argument
print(parrot(voltage=1000))                                  # 1 keyword argument
print(parrot(voltage=1000000, action='VOOOOOM'))             # 2 keyword arguments
print(parrot(action='VOOOOOM', voltage=1000000))             # 2 keyword arguments
print(parrot('a million', 'bereft of life', 'jump'))         # 3 positional arguments
print(parrot('a thousand', state='pushing up the daisies'))  # 1 positional, 1 keyword

# 以下为错误调用方法：
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument
