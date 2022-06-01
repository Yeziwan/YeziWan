print("----------用break函数做终止----------")
for item in range(3):
    a=input("请输入您的账号密码：")
    if a=="161231":
        print("密码正确，请进行后续操作")
        break
    else:
        print("密码错误，请重新输入")

print("-----------用while函数来结算运行次数-----")
a=0
while a<3:
    b = input("请输入您的账号密码：")
    if b=="161231":
        print("密码正确，请进行后续操作")
    else:
        print("密码错误，请重新输入")
        a+=1

# while a>=3 or b=="161231":
#
#     if b=="161231":
#         print("密码正确，请进行后续操作")
#     else:
#         print("密码错误，请重新输入")
#         a+=1