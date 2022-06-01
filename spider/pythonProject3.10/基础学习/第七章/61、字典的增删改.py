scores1={"第一名":"万嘉琦","第二名":"吴渊"}
scores2=dict(第一名="万嘉琦",第二名="吴渊")
print("第一名" in scores1)
print("第三名" not in scores2)
del scores1["第二名"]
print(scores1)
scores2['第三名']="万渊"
print(scores2)
scores2['第二名']='嘉琦'
print(scores2)