infor={"name":"wuyuan","age":24}
print(infor["age"])
print("访问不存在的键值对")
# print(infor["work"])   不存在是会报错
print(infor.get("work"))
print(infor.get("name","30"))
print(infor.get("work","python"))
print("--------增、删、改、查--------")
print("--------增--------")
infor2={"name":"wanjiaqi","age":22}
newID=input("请输入学号")
infor2["id"]=newID
print(infor2["id"])
print(infor2)
