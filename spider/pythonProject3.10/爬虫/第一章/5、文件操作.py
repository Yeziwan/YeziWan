f=open("yezi.txt","w")  #打开文件，W模式（写模式），文件不存在的时候就新建
f.write("hello my wife")

f=open("yezi.txt","r")    #R为读取模式，在该模式下可以读取文件内容
# a=f.read(5)
print(f.read(5))
print(f.read(5))
# f.close()
f=open("yezi.txt","r")
b=f.readlines()  #读很多行
print(b)

f=open("yezi.txt","r")
b=f.readlines()    #读取所有文件，形成列表
i=1
for temp in b:
    print("%d:%s"%(i,temp))
    i+=1
f.close()
# print(b)
f=open("yezi.txt","r")
b=f.readline()
print("1:%s"%b)
b=f.readline()
print("2:%s"%b)

import os
os.rename("yezi.txt","mercy.txt")
f=open("yezi.csv","w")