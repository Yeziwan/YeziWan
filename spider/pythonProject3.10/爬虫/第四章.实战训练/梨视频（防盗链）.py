# -*- coding: UTF-8 -*-
import re
import requests
#1、拿到cont-id
#2、拿到videoinfo中的srcURL
#3、拿到URL后进行替换
#4、下载
url="https://www.pearvideo.com/video_1754307"
# resp=requests.get(url)
# print(resp.text)
contId=url.split("_")[1]
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15",
    "Referer":url
}
videoStatusURL=f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.45726299195665654"
resp=requests.get(videoStatusURL,headers=headers)
dic=resp.json()
srcURL=dic["videoInfo"]["videos"]["srcUrl"]
systemTime=dic["systemTime"]
# print(systemTime)
srcURL=srcURL.replace(systemTime,f"cont-{contId}")
print(srcURL)

with open("a.mp4",mode="wb") as f:
    f.write(requests.get(srcURL).content)
print("下载完毕")
# https://video.pearvideo.com/mp4/adshort/20220314/cont-1754307-15840673_adpkg-ad_hd.mp4
# https://video.pearvideo.com/mp4/adshort/20220314/1647314651790-15840673_adpkg-ad_hd.mp4