# -*- coding:UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import traceback

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillList(list, html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.find_all('div', attrs={'class':'mod-g'}):
            for temp in tag.find_all('div', attrs={'class':'mod-g-detail'}):
                a = temp.find('a')
                p = temp.find('p')
                list.append([a.string, p.string])
        return list
    except:
        print("出错了！")
        return [['1','2','3'],['4','5','6']]

def printList(list):
    print('{:^16}\t{:^16}'.format('第一列','第二列'))
    for i in range(len(list)):
        u = list[i]
        try:  #加这个try语句的意思是为了防止某一列的数据其中一个为NULL，导致出错，现在这样，有问题直接跳过，遍历下一组
            print('{:^16}\t{:^16}'.format(u[0],u[1]))
        except:
            continue

if __name__ == '__main__':
    url = "https://shouji.tmall.com"
    list = []
    html = getHTMLText(url)
    fillList(list, html)
    printList(list)