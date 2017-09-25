# -*- coding:UTF-8 -*-
# 下面的练习代码是自己从天猫收集管简单抓取手机三个信息的练习代码
import requests
import re
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parseWebPage(url) :
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')
    #下面代码可以完成对天猫手机馆页面所有满足给定属性的连接a进行检索，并打印出其中间的字符串
    a = soup.find_all('a', attrs={'target':'_self','href':re.compile("#J_floor\d{1}")})
    for i in a:
        try:
            print(i.string)
        except:
            continue

def getPhoneMess(html):
    list = []
    soup = BeautifulSoup(html, 'html.parser')
    for a in  soup.find_all('div', attrs={'class':'mod-g'}):
        #if isinstance(a, bs4.element.Tag):   #使用isinstance过滤掉空行内容
        for a_temp in a.find_all('div',class_='mod-g-detail'):   #注意，这里是a.find，而不是soup.find，自己第一次写成了soup.find导致出现问题
            alist = a_temp.find('a')
            print(alist.string)
            p = a.find('p')
            print(p.string)

        div = a.find('div', attrs={'class':'mod-g-sales'})   #注意，这里是a.find，而不是soup.find，自己第一次写成了soup.find导致出现问题
        print(div.string)


if __name__ == '__main__':
    url = "https://shouji.tmall.com/"
    html = '''
    <div class="mod-g">
		<a href="//detail.tmall.com/item.htm?acm=lb-zebra-164656-978614.1003.4.2061511&amp;id=558208723934&amp;scm=1003.4.lb-zebra-164656-978614.ITEM_558208723934_2061511" class="mod-g-photo">
			<img src="//g.alicdn.com/s.gif" data-lazyload-src="//img.alicdn.com/tfs/TB1WtCNdgMPMeJjy1XbXXcwxVXa-800-800.jpg" alt="9月11日 小米note3全款预售"/>
		</a>
		<div class="mod-g-detail">
			<h3 class="mod-g-tit"><a href="//detail.tmall.com/item.htm?acm=lb-zebra-164656-978614.1003.4.2061511&amp;id=558208723934&amp;scm=1003.4.lb-zebra-164656-978614.ITEM_558208723934_2061511">9月11日 小米note3全款预售</a></h3>
			<p class="mod-g-desc">自拍美，拍人更美</p>
		</div>
		<div class="mod-g-info">
				<span class="mod-g-nprice">
					<i>&yen;</i>2499
				</span>
			<div class="mod-g-sales">
				已售:9197
			</div>
		</div>
	</div>

	<div class="mod-g">
		<a href="//detail.tmall.com/item.htm?spm=a222r.8260000.4140396539.d1&amp;acm=lb-zebra-164656-978614.1003.4.2061511&amp;id=558531970190&amp;scm=1003.4.lb-zebra-164656-978614.ITEM_558531970190_2061511" class="mod-g-photo">
			<img src="//g.alicdn.com/s.gif" data-lazyload-src="//img.alicdn.com/tfs/TB1NFgsdMMPMeJjy1XdXXasrXXa-800-800.png" alt="9月13日 三星Note8开启预定"/>
		</a>
		<div class="mod-g-detail">
			<h3 class="mod-g-tit"><a href="//detail.tmall.com/item.htm?spm=a222r.8260000.4140396539.d1&amp;acm=lb-zebra-164656-978614.1003.4.2061511&amp;id=558531970190&amp;scm=1003.4.lb-zebra-164656-978614.ITEM_558531970190_2061511">9月13日 三星Note8开启预定</a></h3>
			<p class="mod-g-desc">全视曲面屏  双镜头双防抖</p>
		</div>
		<div class="mod-g-info">
				<span class="mod-g-nprice">
					<i>&yen;</i>6988
				</span>
			<div class="mod-g-sales">
				已售:6326
			</div>
		</div>
	</div>
	'''
    getPhoneMess(html)  #下面是运行结果
    '''
    9月11日 小米note3全款预售
自拍美，拍人更美
				已售:9197
9月13日 三星Note8开启预定
全视曲面屏  双镜头双防抖
				已售:6326
    '''
