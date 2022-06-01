import csv

import requests
import re
import xlwt
url=" https://www.dytt89.com/"
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
}
resp=requests.get(url,headers=headers)
resp.encoding="GBK"
# print(resp.text)
#解析（分两次，第一步拿到区域代码，第二步拿到细节代码）
obj1=re.compile(r'2022必看热片.*?<ul>(?P<bikanurl>.*?)<ul>',re.S)  #第一次筛选
result=obj1.finditer(resp.text)
child_url_list = []
data=[]
for it in result:
    bikanurl = it.group('bikanurl')
    # print(bikanurl)

    obj2=re.compile(r"<a href='(?P<link>.*?)'.*?>(?P<name>.*?)</a><span>",re.S)
    result1=obj2.finditer(bikanurl)
    for i in result1:
        dic1 = i.group()
        print(i.group("link"))
        print(i.group("name"))
        #提取子页面链接
        child_url=url+str(i.group("link")).strip("/")#内层网站
        # print(child_url)
        child_url_list.append(child_url)#封装子链接成列表
        # print(child_url_list)

#提取子页面信息
for link in child_url_list:
    child_resp=requests.get(link,headers=headers)
    child_resp.encoding="GBK"
    # print(child_resp.text)
    ojb3=re.compile(r'>◎片　　名　(?P<name1>.*?)<br />◎年　　代　(?P<years>.*?)<br />.*?'
                    r'>◎豆瓣评分　(?P<rate>.*?)/10 from.*?>◎主　　演　(?P<actors>.*?)'
                    r'◎简　　介<br />　　(?P<info>.*?)<br />.*?'
                    r'<li><a href="(?P<download>.*?)">',re.S)
    resp3=ojb3.search(child_resp.text)
    print(resp3.group("name1"))
    # data.append("name1")
    print(resp3.group("years"))
    # data.append("years")
    print(resp3.group("rate"))
    # data.append("rate")
    print(resp3.group("actors").replace("&middot;","·").replace("<br />","，").replace("&nbsp;","").replace("　　　　　　","").replace("　　　　 　",""))
    # actors=actors.replace("&middot;","·").replace("<br />","，").replace("&nbsp;","").replace("　　　　　　","").replace("　　　　 　","")
    # data.append("actors")
    print(resp3.group("info").replace("&ldquo;","").replace("&middot;","·").replace("&rdquo;","").replace("&hellip;&hellip;",""))
    # data.append("name1")
    print(resp3.group("download"))
    # data.append("name1")
    # f=open("电影天堂2020必看.csv","a",encoding="utf-8",newline="")
    #保存到excel
    # book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    # sheet = book.add_sheet("豆瓣电影top250", cell_overwrite_ok=True)
    # col=("序号","电影名称","上映年份","评分","演员阵容","简介","下载地址",)
    # for i in range(0,7):
    #     sheet.write(0,i,col[i])
    # for i in range(0,20):
    #     print("第%d条"%(i+1))
    #     data=child_url_list[i]
    #     for j in range(0,6):
    #         sheet.write(i+1,0,i+1)
    #         sheet.write(i+1,0,data[j])

    # csvwriter=csv.writer(f)
    # for it in result:
    #     dic=it.groupdict()
    #     dic['actor']=dic['actor'].replace("&middot;","·").replace("<br />","，").replace("&nbsp;","").replace("　　　　　　","")
    #     dic['info']=dic['info'].replace("&ldquo;","").replace("&middot;","·").replace("&rdquo;","").replace("&hellip;&hellip;","")
    #     csvwriter.writerow(dic.values())
    # f.close()
