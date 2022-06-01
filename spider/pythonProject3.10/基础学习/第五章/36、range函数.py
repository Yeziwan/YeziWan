print("------------第一种情况，只有一个元素------------")
a=range(10)#只有一个元素时，元素为结束节点，起点默认从零开始，到终止值前一位结束
print(list(a))
print("------------第二种情况，当有两个元素------------")
b=range(2,10)#有两个元素时，第一个元素为起始值，第二个为终止值
print(list(b))
print("------------第三种情况，当有三个元素------------")
c=range(0,10,2)
print(list(c))
print("------------判断，in、not in、------------")
print(7 in a)
print(7 in c)

print(7 not in a)
print(7 not in c)

print("------------直接打印------------")
print(list(range(1,11,2)))