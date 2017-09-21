# -*- coding:UTF-8 -*-
import requests
import re

def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("")

def getList(list, html):
    try:
        rePrice = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        reTitile = re.findall(r'\"raw_title\"\:\".*?"',html)
        for i in range(len(rePrice)):
            price = eval(rePrice[i].split(":")[1])
            title = eval(reTitile[i].split(":")[1])
            list.append([price, title])
    except:
        print("")

def printList(list):
    count = 0
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    for g in list:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

if __name__ == '__main__':
    goods = "书包"
    dpth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    list = []
    for i in range(dpth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHtmlText(url)
            getList(list, html)
        except:
            continue
    printList(list)
