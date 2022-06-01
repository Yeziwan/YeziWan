list1=[1, 2, 23, 34, 45, 56, 67, 78]
print("一次切换一个元素，使用索引进行定位")
list1[4]=54
print(list1)
list1[5]=[66,77,88]
print(list1)
print("切片，运用区域定位，一次插入多个元素")
list1[2:3]=[11,22,33,44,55]
print(list1)