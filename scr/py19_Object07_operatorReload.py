# coding=utf-8

'''
运算符重载
Python同样支持运算符重载，我么可以对类的专有方法进行重载，实例如下：
'''


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

# 以上代码执行结果如下所示:
# Vector(7,8)
