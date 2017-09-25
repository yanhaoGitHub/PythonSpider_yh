#-*- encoding=UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup
if __name__ == '__main__':
    r = requests.get("http://python123.io/ws/demo.html")
    demo = r.text
    #soup = BeautifulSoup(demo, "html.parser") #第一个参数是要解析的html格式的信息，第二个参数是要使用的解析器
    #print(soup.title)
    #tag = soup.a
    #print(tag.attrs['class'])
    #print(type(tag.attrs))
    #print(soup.a.string)

    #soup2 = BeautifulSoup("<p>中国</p>", "html.parser")
    #print(soup2.p.string)
    #print(soup2.p.prettify())

    soup = BeautifulSoup(demo, "html.parser")
    #print(soup.find_all('p', 'course'))
    #print(soup.find_all(id=re.compile('link')))   这句话和下面这句话意义一样，因为find_all方法用的很多，因此可以直接写(),而省略find_all
    #print(soup(id=re.compile('link')))

    
