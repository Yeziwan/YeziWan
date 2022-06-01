#一、拿到页面源代码
#二、使用BS4进行页面解析，拿到数据
import requests

url="http://www.xinfadi.com.cn/priceDetail.html"
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
}
resp=requests.get(url,headers=headers)
print(resp.text)