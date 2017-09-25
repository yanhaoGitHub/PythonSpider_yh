# -*- coding:UTF-8 -*-
# 下面代码尝试在python3.6版本中使用urllib库
import requests
import whois
import urllib

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

#下面download方法的意思是下载网页，如果中途产生错误，扑捉错误，并且再重试2次下载，总共3次下载，如果3次都下载失败，则退出西程序
def download(url, num_retries=2):
    print("Downloading:" + url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print("DownloadingErr:" + e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <= 600:
                return download(url, num_retries-1)
    return html



if __name__ == '__main__':
    '''
    url = "http://www.baidu.com"
    print(getHTMLText(url))
    '''
    #print(whois.whois('appspot.com'))

    download('http://httpstat.us/500')

