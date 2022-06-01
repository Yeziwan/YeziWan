# -*- coding: UTF-8 -*-
#文档需求：1、商品名称；2、费用；3、公司名称；4、地址；5、成交量
import requests
from lxml import etree
#一、提取页面
url="https://search.zbj.com/f/?kw=saas"
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
}
resp=requests.get(url,headers=headers)
# print(resp.text)
#二、解析页面
html=etree.HTML(resp.text)
# info=html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div/")#拿到所有板块信息
info=html.xpath('//div[@class="new-service-wrap"]/div')
# print(info)

for i in info:
    name="saas".join(i.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))#产品名
    price=i.xpath("./div/div/a[2]/div[2]/div/span[1]/text()")[0].strip("¥")#价格,0代表取消列表
    store=i.xpath('.//*[@id="utopia_widget_76"]/a[1]/div[1]/p/text()')#店名
    count=i.xpath("./div/div/a[2]/div[2]/div/span[2]/text()")[0]#成交量
    address=i.xpath('.//*[@id="utopia_widget_76"]/a[1]/div[1]/div/span/text()')[0]
    # address=i.xpath("./div/div/a/div/div/span/text()")
    # # print(name)
    # # print(price)
    print(store)
    # # print(count)
    # # print(address)