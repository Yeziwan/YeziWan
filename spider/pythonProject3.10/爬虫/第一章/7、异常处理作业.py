def writefile(gushi):
    f=open("gushi.txt","w",encoding="UTF-8")
    for i in gushi:
        f.write(i)
        f.write('\n')
    f.close()
def readline():
    f=open("gushi.txt","r",encoding="UTF-8")
    copy1=f.readlines()
    f.close()
    f=open("copy.txt","w",encoding="UTF-8")
    for i in copy1:
        f.write(i)
        f.write('\n')
    f.close()
str=["落霞与孤鹜齐飞","秋水共长天一色"]
try:
    writefile(str)
    readline()
except Exception as reason:
    print(reason)
finally:
    print("复制完毕")