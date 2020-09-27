# coding=utf-8

# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含0个或1个元素的tuple是个特殊的问题，所以有一些额外的语法规则：

tup1 = ()      # 空元组
tup2 = (20,)   # 一个元素，需要在元素后添加逗号

print(tup1)
print(tup2)
