print("函数的定义")
def printinfor():
    print("-----------------")
    print("人生苦短，我用python")
    print("-----------------")
printinfor()

print("带参数的函数")
def addnum(a,b):
    c=a+b
    print(c)
addnum(12,234)

print("带返回值的函数")
def addnum1(a,b):
    return a+b
result=addnum1(13,123)
print(result)

print("多个返回值的函数")
def chufa(a,b):
    shang=a//b
    yushu=a%b
    return shang,yushu
sh,yu=chufa(13,5)
print("商：%d,余数：%d"%(sh,yu))

print("局部变量")
def test1():
    a=100
    print("test1-------修改前：a=%d"%a)
    a=200
    print("test1-------修改后：a=%d"%a)
test1()       #在函数中为局部变量

def test2():
    a=500     #不同的函数中可以定义相同的名称，不同的函数之间互不相关
    print("test2-------a=%d"%a)
test2()
print("全部变量")
a=500
def test3():
    print(a)
test3()

print("当局部和全局变量的名称相同时，局部优先")
a=1000
def test1():
    a=100      #当想在局部中依然使用全局变量，可以使用 global 函数，可以使所有变量都用全局变量，全局变量修改，局部也修改
    print("test1-------修改前：a=%d"%a)
    a=200
    print("test1-------修改后：a=%d"%a)
test1()       #在函数中为局部变量

def test2():
    print("test2-------a=%d"%a)
test2()