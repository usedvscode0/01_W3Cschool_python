# coding=utf-8

'''
嵌套列表解析
Python的列表还可以嵌套。
以下实例展示了3X4的矩阵列表：
'''
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]

print(matrix)

# 以下实例将3X4的矩阵列表转换为4X3列表：
print([[row[i] for row in matrix] for i in range(4)])
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

print([row[1] for row in matrix])
# [2, 6, 10]

# 以下实例也可以使用以下方法来实现：
transposed1 = []
for i in range(4):
    transposed1.append([row[i] for row in matrix])
print(transposed1)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 另外一种实现方法：
transposed2 = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed2.append(transposed_row)
print(transposed2)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
