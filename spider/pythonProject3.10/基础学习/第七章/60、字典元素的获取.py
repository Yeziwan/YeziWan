scores1={"第一名":"万嘉琦","第二名":"吴渊"}
scores2=dict(第一名="万嘉琦",第二名="吴渊")
print("第一种方式，直接运用'字典名+[]'的方式，注意中括号")
print(scores1["第一名"])
# print(scores1["第三名"])#用中括号的查找，在未查到时回报错，keyerror
print("第二种方式，运用'字典名.get()'的方式，注意使用.get+小括号")
print(scores2.get("第二名"))
print(scores2.get("第三名"))#报错时显示：NONE
print(scores2.get("第四名",1231))
print(type(scores1))
