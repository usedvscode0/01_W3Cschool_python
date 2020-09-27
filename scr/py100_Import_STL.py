# coding=utf-8

import os
import shutil
import glob
import sys
import re
import math
import random
import statistics
import urllib.request
import datetime
import zlib
'''
Python 标准库一览
Python官方教程的最后一个部分就是标准库概览，在这里我们浏览一下标准库，了解一下Python标准库包含了哪些功能。
'''

'''
操作系统和文件操作

os
os模块包含了当前操作系统的抽象，我们可以利用os模块对操作系统进行各种访问。下面使用os模块的几个方法和属性，访问了当前脚本路径、操作系统名以及整个环境变量。
'''
print('--------------os--------------')
print(f'current dir:{os.curdir}')
print(f'os name:{os.name}')
print(f'os path:{os.environ}')
print(f'os linesep:{os.linesep}')

'''
shutil
该模块包含了文件和文件夹的通用工具、包括移动、复制文件和文件夹等等。
'''
print('--------------shutil--------------')

try:
    hosts_file = r'C:\Windows\System32\drivers\etc\hosts'
    dest_file = r'D:\00_FromC\Users\Laputa\Desktop\hosts.txt'
    shutil.copy2(hosts_file, dest_file)
except PermissionError:
    pass

'''
glob
glob模块提供了通配符来选择文件。
'''
print('--------------glob--------------')

source_files = glob.glob('*.py')
print(source_files)

'''
sys
sys模块的argv属性可以获取当前Python脚本执行时的命令行参数。
'''
print('--------------sys--------------')

print(sys.argv)

# sys模块还有几个属性，用于向标准输入、输出、错误流写入和读取数据。例如下面的例子将向标准错误流输出了一些信息。
sys.stderr.write('This is a error\n')

'''
正则表达式
re模块用于处理正则表达式。
下面的例子查找所有以f开头的单词。
'''
print('--------------re--------------')

long_sentence = '''\
When symlinks is false, if the file pointed by the symlink doesn’t exist, an exception will be added in the list of errors raised in an Error exception at the end of the copy process. You can set the optional ignore_dangling_symlinks flag to true
if you want to silence this exception. Notice that this option has no effect on platforms that don’t support os.symlink().
'''
results = re.findall(r'\bf\w+', long_sentence)
print(results)

'''
数学计算

math
math模块包含了很多数学计算的函数。如果需要高级数学计算，可以查阅awesome-python项目查找流行的数学计算模块。
'''
print('--------------math--------------')

print(f'PI is {math.pi}')
print(f'e is {math.e}')

'''
random
random模块包含了一些生成随机数的函数。
'''
print('--------------random--------------')

for i in range(1, 6):
    print(random.choice([1, 2, 3, 4, 5]), end=' ')
print()

for i in range(1, 6):
    print(random.randrange(1, 100), end=' ')
print()

for i in range(1, 6):
    print(random.randint(1, 10), end=' ')
print()

for i in range(1, 6):
    print(random.uniform(1, 10), end=' ')
print()

list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)
print(f'打乱之后:{list1}')

'''
statistics
statistics模块可用于基本的统计。
'''

print('--------------statistics--------------')

data = [1, 2, 3, 4, 5, 6, 7, 4, 5, 6, 2, 3, 4, 4, 4, 4]

print(f'平均数:{statistics.mean(data)}')
print(f'中位数:{statistics.median(data)}')
print(f'方差:{statistics.variance(data)}')
print(f'标准差:{statistics.stdev(data)}')
print(f'众数:{statistics.mode(data)}')

'''
网络

urllib.request和urllib.smtp是处理网络的两个包，用于发起网络请求以及收发电子邮件。
'''

print('--------------urllib.request--------------')

with urllib.request.urlopen('http://www.baidu.com') as web:
    for line in web:
        print(line.decode('UTF8'), end='')

'''
日期时间

datetime模块包含了日期时间的处理。
'''

print('--------------datetime--------------')

today = datetime.date.today()

now = datetime.datetime.today()

print(f'today:{today}')
print(f'now:{now}')

my_age = today - datetime.date(1994, 7, 7)
print(f'my age:{my_age.days/365}')

'''
数据压缩

zlib模块可用于数据压缩。
'''

print('--------------zlib--------------')

data = b'aaaaa bbbbbbb cccccc dddddddd'

compressed = zlib.compress(data)
print(f'data length:{len(data)}, compressed length:{len(compressed)}')

print(f'compressed:{str(compressed)}')
data = zlib.decompress(compressed)
print(f'data:{str(data)}')


'''
其他模块
标准库的模块有很多，这里不介绍了。有兴趣的请直接查看相应资料。
timeit、profile、pstats模块可用于性能测量。
doctest和unittest用于进行测试。
json、xml、csv等模块可以处理相应数据。
sqlite3模块用于处理Sqlite3嵌入式数据库。
    gettext、locale、codecs等模块用于国际化。
'''
