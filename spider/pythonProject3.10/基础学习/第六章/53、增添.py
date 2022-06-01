print("--------在末尾添加一个元素append---------")
list1=[1,2,3,4,5,6,7]
list1.append(11)
print(list1)
print("--------在末尾至少添加一个元素extend---------")
list2=[22,44,33,66,77,88]
# list1.append(list2)
# print(list1)
# list1.extend(list2)
# print(list1)
# print("--------在列表任意位置添加一个元素insert---------")
# list1.insert(2,434)
# print(list1)
print("--------在列表任意位置添加至少一个元素=---------")
list1[3::]=list2
print(list1)