a,b=10,20
print('a>b吗？',a>b)
print('a<b吗？',a<b)
print('a<=b吗?',a<=b)
print('a>=b吗？',a>=b)
print('a==b吗？',a==b)#一个等号=表示赋值运算符，两个等号==表示比较运算符，
#一个等号表示，赋值，令a的值等于b，两个等号表示做比较，a是否等于b
print('a!=b吗？',a!=b)
print(a==b)
print(a is b)
print(a is not b)
list1=[33,44,55,66]#值相同，id不同
list2=[33,44,55,66]
print(id(list1))
print(id(list2))
print(list1==list2)
print(id(list1)==id(list2))