# -*- coding: UTF-8 -*-#
#BeautifulSoup是将复杂的HTML文档转化成一个复杂的属性结构图，每个节点都是python对象
#所有对象可分为四种：
from bs4 import BeautifulSoup
import re
#1、先读
file=open("./百度.html","rb")  #以rb的格式阅读
html=file.read().decode("utf-8")  #先读到html中
bs=BeautifulSoup(html,"html.parser")   #使用BeautifulSoup来解析html，使用parser的格式


# # print(bs.title)
# # print(bs.a)
# # print(bs.head)
# print(type(bs.head))   #引出第一个对象类型，tag
# #1、tag，标签及其内容，拿到他找到的第一个标签中的内容
#
#
# print(bs.title)
# print(bs.title.string)
# print(type(bs.title.string))  #引出第二个类型，NavigableString
# #2、NavigableString，标签里的内容，以字符串的形式呈现


# print(bs.a)
# print(bs.a.attrs)
# print(type(bs.a.attrs))   #以键值对的形式呈现
#
#
# print(type(bs))     #引出第三种类型BeautifulSoup
# #3、第三种类型，他自身
#
# print(bs.a.string)
# print(type(bs.a.string))   #引出第四种类型
# #4、common，是一个特殊的NavigableString，输出的内容不含注释的部分
#
# #-------------------------------------------
#
# #文档遍历
# # print(bs.head.contents)
# # print(type(bs.head.contents))    #列表类型
# print(bs.head.contents[1])

# #一、文档搜索
# #1、find_all()
# #1.1字符串过滤：查找所有与字符串完全匹配的内容
# t_list=bs.find_all("a")  #找到所有a标签
# print(t_list)


# #1.2正则表达式搜索：使用search（）方法进行匹配搜索
# t_list=bs.find_all(re.compile("a"))
# print(t_list)


# #1.3方法：传入一个函数（方法），根据函数的要求来搜索
# def name_is_exists(tag):    #创建一个函数，搜索tag中所有带name的部分，返回值
#     return tag.has_attr("name")
# t_list=bs.find_all(name_is_exists)
# for item in t_list:
#     print(item)
# # print(t_list)

#2、kwargs参数
# t_list=bs.find_all(id="head")    #存在id=head的部分
# t_list=bs.find_all("class")
# t_list=bs.find_all(class_=True)  #class存在的部分
# for item in t_list:
#     print(item)

#3、text参数
# t_list=bs.find_all(text="hao123")   #查特定文本，可以放列表
# t_list=bs.find_all(text=["hao123","新闻","地图"])
# t_list=bs.find_all(text=re.compile("\d"))   #\d表示所有包含数字的
# for item in t_list:
#     print(item)

# #4、limit参数   限定获取信息的个数
# t_list=bs.find_all("a",limit=3)
# for item in t_list:
#     print(item)


# #二、css选择器
# t_list=bs.select('title')   #通过标签来查找
# t_list=bs.select('.mnav')   #通过类名来查找
# t_list=bs.select("#u1")     #通过ID来查找
# t_list=bs.select("a[class='bri']")  #通过属性来查找
# t_list=bs.select("head>title") #通过子标签，一级一级向下查找
try:
    t_list=bs.select(".mnav~ .bri")  #兄弟标签
    print(t_list[1].get_text())
except IndexError as e:
    print(e)
# for item in t_list:
#     print(item)