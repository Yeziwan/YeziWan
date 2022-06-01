print("本章重点：remove,pop,切片,clear,del")
list1=[1, 2, 3, 22, 44, 33, 66, 77, 88,33,22,44]
print("---------remove一次删除一个元素---------")
list1.remove(33)
print(list1)
# list1.remove(324)
# print(list1)
print("---------pop删除指定位置的元素，若未指定，删除最后一个---------")
list1.pop(4)
print(list1)
list1.pop()
print(list1)
print("---------切片，选取一段，其他删掉---------")
list2=list1[5:7]
print(list2)
list3=[23,34,45,56,67,78]
list1[2::]=list3
print(list1)
list2=list1[3:7]
print(list2)
print("---------clear清空列表---------")
list2.clear()
print(list2)
print("---------del删除列表---------")
del list1
