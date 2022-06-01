a=int(input("num_1"))
b=int(input("num_2"))
# if a>b:
#     print(a,"大于",b)
# else:
#     if a==b:
#         print(a,"等于",b)
#     else:
#         print(a,"小于",b)
print((a,"大于等于",b) if a>=b else (a,"小于",b))
print((str(a)+"大于等于"+str(b)) if a>=b else (str(a)+"小于"+str(b)))#用+，类型转换成str,表达更优秀

