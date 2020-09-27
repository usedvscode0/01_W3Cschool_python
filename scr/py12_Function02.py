# coding=utf-8

# 更复杂点的应用，函数中带上参数变量:

def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Fred")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

# 以上实例输出结果：
# Welcome Fred
# width = 4  height = 5  area = 20
