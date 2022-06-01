print("----------创建元组----------")
tuple1=()#  空元组
tuple2=(50)#  定义为字符串
tuple3=(50,)#  有逗号，定义为元组
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print("----------元组的增删改查----------")
tuple4=(45,56,67,78)#（0，1，2，3）
print(type(tuple4))
print(tuple4[1])
print(tuple4[-1])
print(tuple4[1:3])#左闭右开
print("tuple增")
tuple5=(232,4345,656)
tuple=tuple4+tuple5#并不是在原有基础上进行改正，而是创建了一个新的元组
print(tuple)
print("tuple删")
# del tuple3#  删除整个元组，后续无法查到
# print("删除后")
# print(tuple3)
print("元组的其他用法")
print(656 in tuple)
print(tuple.count(0))
print(tuple.count(67))
print(len(tuple))
print(max(tuple))
print(min(tuple))
# print(tuple(tuple2))#将其他类型转变为元组
