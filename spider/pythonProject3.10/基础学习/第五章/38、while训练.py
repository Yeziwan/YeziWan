print("-------制作1-100之间的偶数和---------")
a=1
sum=0
while a<=100:
    if a%2==0:#另一种写法 if not bool(a%2);
        sum+=a
        a+=1
    else:
        a=a+1
print("和为：",sum)

#˜
# # if a%2==0:
# #     pass
# b=range(0,101,2)
# print(sum(b))