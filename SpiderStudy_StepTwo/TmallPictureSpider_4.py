# -*- coding:UTF-8 -*-
# 下面代码实现的功能是对天猫手机管中的图片进行爬取图片并下载到本地文件夹
# 但是在爬取链接的时候，自己想用正则表达式，但是没成功
import requests
import re
import os
from bs4 import BeautifulSoup

def getHTMLText(url) :
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

#得到所要下载的图片的链接，并且放在列表中
def getPicList(list, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all('img'):
        #pic = tag.get(re.('data-lazyload-src|data-ks-lazyload'))
        pic = tag.get('data-ks-lazyload')
        if pic != None:
           list.append(pic)
    return list

def downLoadPic(list):
    path = "D:/TmallPics"
    urlStart = "http:"
    count = 1
    #目录已经存在，不需要重新创建
    if os.path.exists(path):
        print("目录已经存在，不需要重新创建!")
    #如果文件夹目录不存在，则创建文件夹
    else:
        os.mkdir(path)
        print("文件夹创建成功！")

    for picNum in range(len(list)):
        url = urlStart + list[picNum]  #构造出最后需要下载的url
        print(url)
        r = requests.get(url)
        with open(path+'/'+str(count)+'.jpg', 'wb') as f:
            count = count + 1
            f.write(r.content)
            f.close()

if __name__ == '__main__':
    url = "https://shouji.tmall.com"
    list = []
    html = getHTMLText(url)
    getPicList(list, html)
    downLoadPic(list)