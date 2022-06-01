# print("else 和for函数一起使用")
# for a in range(3):
#     b=input("请输入密码：")
#     if b=="161231":
#         print("输入正确")
#         break
#     else:
#         print("输入错误，请重新输入")
# else:
#     print("三次错误，账户冻结")
# print("else 和while函数一起使用")
a=0
while a<3:
    b=input("请输入密码：")
    if b=="161231":
        print("输入正确")
        break
    else:
        print("输入错误，请重新输入：")
        a+=1
else:
    print("三次错误，账户冻结")