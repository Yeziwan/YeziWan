print("--------100至999之间的水仙花数的数量--------153=3*3*3+5*5*5+1*1*1")
print("--------第一种解答方式--------")
for a in range(100,1000):
    if a==(a%10)**3+((a//10)%10)**3+((a//100))**3:
        print((a))

# print(153%10)
# print((153//10)%10)
# print(153//100)
# print(list(a))

# sum=0
# for a in range(100,1000):
#     for b in str(a):
#         for c in int(b):
#             if sum(c**3)==a:
#                 print(a)
# a=175
# for s in range (175,175):
#
#     for x in range(s):

# axe=0
# for s in str(175):
#     # print(s)
#     for x in s:
#         x=int(x)
#         axe+=x**3
#         print(axe)
#         # if axe==s:
#         #     print(s)

# a=153
# sum=0
# for b in str(a):
#     b=int(b)
#     sum+=b**3
#     if sum==a:
#         print(sum)

# sum=0
print("---------第二种解题思路---------病痛")
for n in range(100,1000):
    # for s in str(n):
    #     for x in s:
    #         x=int(x)
    #         sum+=x**3
    #         if sum==n:
    #             print(sum)

    if sum([x**3 for x in [int(s) for s in str(n)]])==n:
        print(n)
# for n in range(100,1000):
#     for s in str(n):
#         for x in int(s):
#             sum(x**3)