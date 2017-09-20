#-*-encoding = UTF-8 -*-
import requests

if __name__ == '__main__':
    r = requests.get('http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html')
    print(r.status_code)
    r.encoding = r.apparent_encoding
    print(r.text)