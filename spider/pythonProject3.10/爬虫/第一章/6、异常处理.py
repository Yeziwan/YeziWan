# print("------------捕获异常------------")
# try:     #捕获异常
#     print("----1----")
#     a=open("yezi.txt","r")
#     print("----2----")
# except IOError:   #IOError
#     pass
# try:
#     print(num)
# except NameError:
#     pass
#
# try:
#     print("----1----")
#     a=open("yezi.txt","r")
#     print("----2----")
#     print(num)
# except Exception as reason:
#     print("报错")
#     print(reason)
#
# try:
#     print("----1----")
#     a=open("yezi.txt","r")
#     print("----2----")
#     print(num)
# except (FileNotFoundError,NameError) as reason:
#     print("报错")
#     print(reason)

print("----finally----")
import time
try:
    f=open("mercy.txt","r")
    try:
        while True:
            content=f.readline()
            if len(content)==0:
                break
            time.sleep(1)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except FileNotFoundError:
    print("发生异常")