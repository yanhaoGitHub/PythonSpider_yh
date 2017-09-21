# -*- coding:UTF-8 -*-
# 下面的代码运行会出现部分异常，但是这个异常并不是程序本身造成的，而是网页的源代码之中a标签的属性缺失导致解析到的对象为null，从而导致部分网页的信息出现问题
# 但是仍然能够生成一个文件，其中依然包含了很多的股票信息！
# 教训：：：在做大型爬虫之前，需要考虑好爬取页面的html代码的一致性!不能说属性不同导致同样的代码解析有的网站就可以，而解析另一些网站就不行
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


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)  # 调用第一个函数，得到这个所有股票的页面信息
    soup = BeautifulSoup(html, "html.parser")  # 使用html解析器解析上面得到的这个html页面
    a = soup.find_all('a')  # 查看网页源代码之后发现，所有与股票代码有关的内容都报存在a标签中，因此得到所有的a标签进行遍历
    # print("a标签的类型是:" + type(a))
    for i in a:
        try:
            href = i.attrs['href']  # 这行代码的意思是针对每一个a链接，使用href属性对应的后面的值，即我们需要的链接
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])  # 因为findall函数会以列表形式返回匹配后的字符串，所以使用[0]来获取该链接
        except:
            continue


def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + stock + ".html"  # 公共连接部分加上每个股票单独的部分形成最终的url链接
        html = getHTMLText(url)  # 得到各股的信息页面
        try:
            if html == "":
                continue
            infoDict = {}

            soup = BeautifulSoup(html, "html.parser")  # 构建解析器，并对该页面完成解析
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})  # 先找到大概位置

            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]  # 在大概位置处，进行详细查找
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
        except:
            traceback.print_exc()  # 如果产生错误，我们使用traceback来得到错误信息
            continue


if __name__ == '__main__':
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D://BaiduStockInfo.txt'  # 将最后的结果保存在D盘根目录文件下
    slist = []
    getStockList(slist, stock_list_url)  # 首先获得股票列表
    getStockInfo(slist, stock_info_url, output_file)
