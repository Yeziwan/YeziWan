# # -*- coding: UTF-8 -*-
# #时间
# import time
# import datetime
# import calendar
# #获取URL
# import urllib.request
# #解析URL
# from bs4 import BeautifulSoup
# #获取图片
# import requests
# #获取验证码
# import pytesseract
# #获取验证码图片
# from PIL import Image
# #获取验证码图片
# from io import BytesIO
# #获取验证码图片
# import base64
# #获取验证码图片
# import json
# #获取验证码图片
# import re
# #获取验证码图片
# import os
# #获取验证码图片
# import sys
# #99乘法口诀
# import math

#创建一个函数
import urllib
import urllib.request

def get_html(url):
    #获取网页
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    #设置头部
    req = urllib.request.Request(url, headers=headers)
    #设置请求
    html = urllib.request.urlopen(req).read()
    #读取网页
    html = html.decode('utf-8')
    #解码
    return html

get_html("https://leetcode-cn.com")