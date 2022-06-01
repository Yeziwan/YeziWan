# -*- coding: UTF-8 -*-
import re
# #一、创建模式对象    pat有模式对象的情况使用
# pat=re.compile("aa")  #此处的aa为正则表达式，用来检验其他的字符串
# m=pat.search("ssaddaadd")    #search是被aa检验的内容
# m=pat.search("aassaddaadd")  #从左到右依次进行，检查到后即停止运行
# print(m)


#二、没有模式对象     re没有模式对象的
m=re.search("aaa","asdasdaaaassaa")    #前面的字符串是规则，后面的是被校验的对象
print(m)


#findall全局搜索
print(re.findall("a","sadsadadsad")) #findall全局搜索
print(re.findall("[A-Z]","sadssaSAXsSSadsXXAd"))   #单个搜索
print(re.findall("[A-Z]+","sadssaSAXsSSadsXXAd"))  #+加号为正则表达式

#sub
print(re.sub("a","A","sadssaSAXsSSadsXXAd"))       #用第二个"A"去替换校验对象中的"a"


#在正则表达式中，被比较的字符串前加上r，不用担心转义字符的问题
a="\e13se\'"
b=r"\e13se\'"    #字符串加上
print(a)
print(b)    #比较a和b，a中的\为被打印，系统认为\是转义字符，b中的被比较字符串加了r，不受影响