print("画一条横线")
def line():
    print("-"*30)
line()
print("--------------运用以上函数，画多条横线--------------")
# print("运用for循环来做")
# num=int(input("请输入横线数量："))
# def numline(num):
#     for a in range(0,num):
#         line()
#         a=a+1
# numline(num)
# print("运用while循环来做")
# num=int(input("请输入横线数量："))
# def numline(num):
#     a = 0
#     while a<num:
#         line()
#         a+=1
# numline(num)
# print("--------------求三个数的和--------------")
def add1(a,b,c):
    return a+b+c
print(add1(34,45,65))
#     d=a+b+c
#     print(d)
# add1(23,32,11)
print("--------------求三个数的平均值--------------")
def ave(a,b,c):
    d=add1(a,b,c)
    f=d/3
    return f
print("平均值为：%d"%ave(113,12,312))