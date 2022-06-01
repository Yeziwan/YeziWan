a=float(input("渊哥的面试分数"))#此处使用float既可以输入整数，也可以输入小数，使用int只能输入整数
if a>=90:
    print(a,"极佳")
else:
    if 80<=a<90:#if a>=80 and a<90:只有python语言可以这样使用
        print(a,"优秀")
    else:
        if 70<=a<80:
            print(a,"良好")
        else:
            if 60<=a<70:
                print(a,"及格")
            else:
                print(a,"不及格")
# a=input("输入")
# # print(int(3.1234))
# # print(float(3.1234))
# if int(a)-float(a)==0:
