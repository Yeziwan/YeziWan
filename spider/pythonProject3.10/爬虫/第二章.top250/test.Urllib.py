# -*- coding: UTF-8 -*-
#获取一个get请求
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request

# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))

#获取一个post请求  模拟用户登陆

# import urllib.parse
# data=bytes(urllib.parse.urlencode({}),encoding="utf-8")  #封装data数据，用data再表述response
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))


# #超时处理，假如被识别为爬虫，拒绝访问，可以设置超时相应，时间过后继续下一个进程
# try:
#     response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.1)   #被检测出为爬虫
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as reason:
#     print(reason)
# print("已超时")

# response=urllib.request.urlopen("http://douban.com")
# print(response.status)    #报错418表示对方已识别出我为爬虫

# response=urllib.request.urlopen("http://www.baidu.com")   #获取头部信息
# print(response.getheader("Server"))



#访问豆瓣，防止被反爬虫检测
url="http://movie.douban.com/top250"
headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
}
req=urllib.request.Request(url=url,headers=headers)  #封装基础信息,做伪装
request=urllib.request.urlopen(req)   #伪装之后再打开网站
print(request.read().decode("utf-8")) #根据伪装信息，进入网站