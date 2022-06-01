# -*- coding: UTF-8 -*-


#get方式
# import requests
# query=input("输入你想查询的事物")
# url=" https://www.baidu.com/s?wd={query} "
# headers={
# "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
# }
# resp=requests.get(url,headers=headers)
# print(resp)
# print(resp.text)   #拿到页面源代码


# #post方式
# import requests
# url=" https://fanyi.baidu.com/sug"
# fanyi=input("请输入你想翻译的内容")
# dat={
#     "kw": fanyi
# }
# resp=requests.post(url,data=dat)
# print(resp)
# print(resp.json())   #json将服务器返回的内容直接处理成字典

import requests
# #重新封装参数
# url="https://movie.douban.com/j/chart/top_list"
# param={
#     "type": "24",
#     "interval_id": "100:90",
#     "action":" ",
#     "start": 0,    #可自定义起始值
#     "limit": 100,  #每页多少数据
#
# }
# headers={
# "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
# }
# resp=requests.get(url=url,params=param,headers=headers)
# print(resp.json())
url="https://movie.douban.com/top250?start="
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
}

for i in range(0,10):
    resp = requests.get(url=url, headers=headers)
    url=url+str(i*25)
    print(resp.text)

    r'>◎豆瓣评分　(?P<rate>.*?)/10 from.*?'
    r'>◎主　　演　(?P<actors>.*?)<br />◎标　　签　.*?'
    r'>◎简　　介<br />　　(?P<info>.*?)<br />◎获奖情况<br />.*?'
    r'<li><a href="(?P<download>.*?)">'
    r'◎简　　介<br />(?P<info>.*?)<br />◎获奖情况<br />.*?'
    r'<li><a href="(?P<download>.*?)">'