# -*- coding: UTF-8 -*-
import csv
import requests
import re
#一、拿到整个页面
baseurl = "https://movie.douban.com/top250?start="
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
}
for i in range(0,10):
    url = baseurl + str(i * 25)
    resp=requests.get(url,headers=headers)
    # print(resp.text)
    page_info=resp.text
    #二、解析页面
    obj=re.compile(r'<li>(.*?)<span class="title">(?P<name>.*?)</span>(.*?)'
                       r'<p class="">(.*?)<br>(?P<years>.*?)&nbsp(.*?)'
                       r'<span class="rating_num" property="v:average">(?P<rate>.*?)</span>(.*?)'
                       r'<span>(?P<judg>.*?)人评价</span>',re.S)
    result=obj.finditer(resp.text)
    f=open("豆瓣top250.csv","a",encoding="utf-8",newline="")
    csvwriter=csv.writer(f)
    for it in result:
    #     dic=it.groupdict()
    #     dic['years']=dic['years'].strip()
    #     csvwriter.writerow(dic.values())
    # f.close()
        print(it.group("name"))
        # print(it.group("years").strip())
        # print(it.group("rate"))
        # print(it.group("judg"))

