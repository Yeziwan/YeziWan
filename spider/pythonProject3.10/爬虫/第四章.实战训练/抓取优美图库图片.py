# -*- coding: UTF-8 -*-
#库
import re

import requests
from bs4 import BeautifulSoup
#第一步：抓取页面
#第二步：提取页面子链接
#第三步：进入子链接，找到下载地址
#第四步：下载图片


#方法一：用正则表达式
#re库
# ojb1=re.compile(r'<li><a href="(?P<link>.*?)" class=',re.S)
#
# #1、抓取页面
# url="https://www.umeitu.com/weimeitupian/"
# headers={
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
# }
# resp=requests.get(url,headers=headers)
# resp.encoding="utf-8"
# # print(resp.text)
# #2、提取子页面链接
# ojb1=re.compile(r'<li>.*?<a href="/weimeitupian/(?P<link>.*?)" class="TypeBigPics.*?/><span>(?P<name>.*?)</span></a>',re.S)
# ojb2 = re.compile(r'<img src="(?P<download>.*?)" /></p> </div>', re.S)
# result1=ojb1.finditer(resp.text)
# for it in result1:
#     # print(it.group('link'))
#     print(it.group('name'))
#     urlall=url+str(it.group('link'))
#     print(urlall)
# #第三步，进入子链接，找到下载地址
#     resp2=requests.get(urlall,headers=headers)
#     resp2.encoding="utf-8"
#     # print(resp2.text)
#     result2 = ojb2.finditer(resp2.text)
#     for i in result2:
#         print(i.group('download'))



#方法二：用BS4
#1、抓取页面
url="https://www.umeitu.com/weimeitupian/"
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
}
obj1=re.compile(r'<strong>(?P<name>.*?)</strong>')
resp=requests.get(url,headers=headers)
resp.encoding="utf-8"
# print(resp.text)
#2、使用BS4进行解析
main_page=BeautifulSoup(resp.text,"html.parser")
alist=main_page.find("div",class_="TypeList").find_all("a")
# print(alist)
for a in alist:
    # print(a.get("href").replace("/weimeitupian/",""))
    child_url=url+str(a.get('href')).replace("/weimeitupian/","")
    # print(child_url)
    child_resp=requests.get(child_url,headers=headers)
    child_resp.encoding="utf-8"
    # print(child_resp.text)
    main_child_page=BeautifulSoup(child_resp.text,"html.parser")
    child_list=main_child_page.find("div",class_="ImageBody")
    # child_list_title=main_child_page.find("div",class_="relax-arc")
    # nameimg=child_list_title.find("img")
    # print(nameimg.get("title"))
    # print(child_list_title)
    # for b in child_list_title:
    #     print(b.find("title"))

    # print(child_list)
    img=child_list.find("img")
    src=img.get("src")
    print(img.get("src"))
    result1=obj1.finditer(child_resp.text)
    for c in result1:
        filename=c.group("name")
        print(c.group("name"))
#3、下载图片
        resp_img=requests.get(src)
        img_name=filename
        with open(img_name,mode="wb") as f:
            f.write(resp_img.content)
        print("over",img_name)
print("all over")