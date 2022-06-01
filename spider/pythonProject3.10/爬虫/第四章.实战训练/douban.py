# # -*- coding: UTF-8 -*-
import re

import requests
#
# # url="https://blog.csdn.net/weixin_43148062/article/details/105639146"
# # headers={
# #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
# # }
# # ojb1=re.compile(r'<dt><span class="count">(?P<count>.*?)</span></dt>.*?'
# #                 r' <dd class="font">(?P<name>.*?)</dd>',re.S)
# # resp=requests.get(url,headers=headers)
# # # print(resp.text)
# # it=list(ojb1.finditer(resp.text))
# # for x in it:
# #     print(x.group("count"))
# #     print(x.group("name"))
# url="https://movie.douban.com/top250"
# headers={
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
# }
# resp=requests.get(url,headers=headers)
# print(resp.text)
# obj=re.compile(r'<img width="100" alt="(?P<name>.*?)" src="',re.S)
# result=obj.finditer(resp.text)
# for i in result:
#     print(i.group("name"))
url="https://www.umeitu.com/weimeitupian/yijingtupian/244666.htm"
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
}
resp=requests.get(url,headers=headers)
resp.encoding="utf-8"
print(resp.text)
ojb2 = re.compile(r'<img src="(?P<download>.*?)" /></p> </div>', re.S)
result2=ojb2.finditer(resp.text)
for i in result2:
    print(i.group('download'))