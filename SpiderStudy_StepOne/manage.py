# -*- encoding=UTF-8 -*-
import requests

def err_process(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取内容失败！"

if __name__ == '__main__':
    #url = "http://www.baidu.com/robots.txt"
    url = "http://www.moe.edu.cn/robots.txt"
    print(err_process(url))