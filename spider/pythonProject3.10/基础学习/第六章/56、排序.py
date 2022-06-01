list1=[1, 2, 11, 22, 33, 44, 55, 34, 54, 67, 78]
print("----------sort用法,加上reverse=Ture表示倒序排列------------")
print("----------sort用法,在原有列表上进行修改，不改变列表ID------------")
print(list1,id(list1))
list1.sort()
print(list1,id(list1))
list1.sort(reverse=True)
print(list1,id(list1))
print("----------sorted用法，内置函数,在选择列表后插入reverse=Ture即表示倒叙-------------")
print("----------sorted用法，内置函数,改变原有列表ID，相当于创建了一个新列表-------------")
list1=sorted(list1)
print(list1,id(list1))
list1[2]=90
list1[3:6]=[11,87,99,55,32,55,77]
print(list1,id(list1))
list1=sorted(list1,reverse=True)
print(list1,id(list1))