# coding=utf-8

# Sets（集合）
# 集合（set）是一个无序不重复元素的集。
# 基本功能是进行成员关系测试和消除重复元素。
# 可以使用大括号 或者 set()函数创建set集合，注意：创建一个空集合必须用 set() 而不是 { }，因为{ }是用来创建一个空字典。

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)   # 重复的元素被自动去掉

print('Rose' in student)

student2 = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 111}
print(student2)
