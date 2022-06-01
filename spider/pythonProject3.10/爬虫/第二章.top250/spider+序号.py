# conding=utf-8
import sys
import bs4 #网页解析，获取数据
from bs4 import BeautifulSoup       #网页解析，获取数据
import re #正则表达式，进行文字匹配
import urllib.request,urllib.error  #制定URL，获取网页数据
import xlwt    #进行Excel操作
import sqlite3      #进行SQLite数据库操作
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

baseurl="https://movie.douban.com/top250?start="
def main():
    # baseurl="https://movie.douban.com/top250?start="
    # if __name__ == "__main__":
    #     main()
    #1、爬取网页
    datalist=getData(baseurl)  #定义获取数据的列表
    savepath="豆瓣爬虫top250.xls"
    dbpath="movie.db"
    #2、解析数据
    #3、保存数据
    savedata(datalist,savepath)
    # savedata2DB(datalist,dbpath)
    askurl("https://movie.douban.com/top250?start=")


#影片详情中文名称的规则
#创建正则表达式对象，表示字符串模式
findName=re.compile(r'<span class="title">(.*)</span>')    #检测中文名称
# findEName=re.compile(r'<span class="title">(.*?)</span>') #检测英文名称
findImgSrc=re.compile(r'<img .* src="(.*?)"',re.S)    #检测图片，re.S 让换行符包含在字符中
findLink=re.compile(r'<a href="(.*?)">')     #检测电影链接
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')#电影评分
findJudge=re.compile(r'<span>(\d*)人评价</span>')#电影评价人数
findInq=re.compile(r'<span class="inq">(.*)</span>')#电影评价
findBD=re.compile(r'<p class="">(.*?)</p>',re.S)#相关信息
#一、爬取网页
#1.1爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(0,10):
        url=baseurl+str(i*25)
        html=askurl(url)   #将获取到的网页源码保存
        # print(html)
#1.2逐一进行解析
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):
            # print(item)     #打印item
            data=[]
            item=str(item)
            #检索名字
            name=re.findall(findName,item)      #名字不止一个
            if(len(name))==2:        #如果名字（title）有两个
               Cname=name[0]         #中文名字选第一个
               data.append(Cname)
               # Oname=name[1].replace("/","")         #英文名字选第二个,去掉/
               Oname = name[1].replace("\xa0/\xa0", "")
               data.append(Oname)
            else:
               data.append(name[0])  #如果名字只有一个，只输出第一个
               data.append(" ")      #第二个留空，空行，但不能不留
            #检索图片
            imgSrc=re.findall(findImgSrc,item)[0]     #0表示只要多个中的第一个
            data.append(imgSrc)
            #检索链接
            Link=re.findall(findLink,item)[0]
            data.append(Link)
            #检索评分
            Rating=re.findall(findRating,item)[0]
            data.append(Rating)
            #检索评价人数
            Judge=re.findall(findJudge,item)[0]
            data.append(Judge)
            if len(Inq)!=0:
                Inq=Inq[0].replace("。","")     #添加句号
                data.append(Inq)
            else:
                data.append(" ")    #留空
            #检索附件
            BD=re.findall(findBD,item)[0]
            BD=re.sub('<br(\s+)?/>(\s+)?'," ",BD)  #去掉br
            BD=re.sub('/'," ",BD)             #替换/
            BD=re.sub('\xa0'," ",BD)
            data.append(BD.strip())           #去掉前后的空格

            datalist.append(data)             #把处理好的一部电影信息放入datalist





            # Ename = re.findall(findEName, item)[1]
            # #re库用来通过正则表达式查找指定的字符串
    print(datalist)     #测试检索的信息
            # print(Ename)
    return datalist
#1.2得到一个指定网站的URL
def askurl(url):
    head={"User-Agent":" Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
          }#用于伪装，并告诉服务器我们可以接受什么类型的信息
    request= urllib.request.Request(url=url, headers=head)  # 封装基础信息,做伪装
    html=""
    try:
        response = urllib.request.urlopen(request)  # 伪装之后再打开网站
        html=response.read().decode("utf-8")
        # print(html)   #打印html
    except urllib.error.URLError as e:
        if hasattr(e,"code"):#"code"检测reason中是否包含了code这个属性
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html




#
# def getData(baseurl):
#     datalist=[]
#     return datalist   #返回解析数据

#保存数据
def savedata(datalist,savepath):
    print(savedata)
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet("豆瓣电影top250",cell_overwrite_ok=True)
    col=("序号","电影中文名","电影外文名","图片","链接","评分","评价人数","概述","附件")
    for i in range(0,9):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%(i+1))
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,0,i+1)
            sheet.write(i+1,j+1, data[j])   #数据表
    book.save(savepath)   #保存


# def savedata2DB(datalist,dbpath):
#     init_db(dbpath)
#     conn=sqlite3.connect(dbpath)
#     cur=conn.cursor()
#
#
#     for data in datalist:
#         for index in range(len(data)):
#             if index==4 or index==5:
#                 continue
#             data[index] = '"'+data[index]+'"'
#         sql='''
#             insert into 豆瓣电影top250(
#             cname,ename,pic_link,info_link,score,rated,instroduction,info)
#             values(%s)'''%",".join(data)
#         # print(sql)
#         cur.execute(sql)
#         conn.commit()
#     cur.close()
#     conn.close()
#
#
# def init_db(dbpath):
#     sql='''
#     create table 豆瓣电影top250
#     (
#     id integer primary key autoincrement,
#     cname varchar,
#     ename varchar,
#     pic_link text,
#     info_link text,
#     score mumeric,
#     rated mumeric,
#     instroduction text,
#     info text
#     )
#
#     '''
#     conn=sqlite3.connect(dbpath)
#     cursor=conn.cursor()
#     cursor.execute(sql)
#     conn.commit()
#     conn.close()
#     # print("建表成功")


#     print("nihao")
#
if __name__=="__main__":  #当程序执行时
    main()    #调用函®数
# if __name__=="__main__":
#     init_db("movie.db")
    print("爬取完毕")