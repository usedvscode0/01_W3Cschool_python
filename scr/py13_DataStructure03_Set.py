# coding=utf-8

'''
集合
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典，下一节我们会介绍这个数据结构。
以下是一个简单的演示：
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)    # show that duplicates have been removed
# {'orange', 'banana', 'pear', 'apple'}

print('orange' in basket)    # fast membership testing
# Ture

print('crabgrass' in basket)
# False

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)    # unique letters in a
# {'a', 'r', 'b', 'c', 'd'}
print(a - b)    # letters in a but not in b
# {'r', 'd', 'b'}
print(a | b)    # letters in either a or b
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)    # letters in both a and b
{'a', 'c'}
print(a ^ b)    # letters in a or b but not both
# {'r', 'd', 'b', 'm', 'z', 'l'}
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # show that duplicates have been removed
# {'orange', 'banana', 'pear', 'apple'}
print('orange' in basket)   # fast membership testing
# True
print('crabgrass' in basket)
# False

# 集合也支持推导式：
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
# {'r', 'd'}
