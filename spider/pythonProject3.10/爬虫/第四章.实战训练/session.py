# -*- coding: UTF-8 -*-
import requests
#1、回话，用处：获取loginname（用户名），password（密码）
session=requests.session()
data={
    #存放账号密码
}
#2、登录
url=""#登录界面的URL
resp=session.post(url,data=data)
#print(resp.text)
#3、拿书架上的书
resp1=session.get()#书架界面的URL
# print(resp1.text)


#二、暴力解法
headers=""
cookie=""
resp=requests.get(url=url,headers=headers,cookies=cookie )
print(resp.text)