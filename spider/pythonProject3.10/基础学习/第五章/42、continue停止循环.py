print("-----要求输出1-50之间所有5的倍数-----")
print("方法一")
for a in range(1,50):
    if a%5==0:
        print(a)
    else:
        pass
print("方法二")
# a=1
# while a<50:
#     if a%5!=0:
#         a+=1
#     else:
for c in range(1,50):
    if c%5!=0:
        continue
    else:
        print(c)