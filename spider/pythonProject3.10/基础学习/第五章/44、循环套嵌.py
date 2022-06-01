# print("制作一个三行四列的矩形")
# for a in range(0,3):
#     for b in range(0,4):
#         print("*",end="\t")#\t表示输出时不换行
#     print()
# print("制作一个空心的三行四列矩形")
# for a in range(0,3):
#     for b in range(0,4):
#         if (a==1 and b==1) or (a==1 and b==2):
#             print(" ",end="\t")
#         else:
#             print("*", end="\t")  # \t表示输出时不换行
#     print()
print("制作99乘法口诀表")
for a in range(1,10):
    for b in range(1,a+1):
        print(a,"*",b,"=",a*b,end="\t")
    print()