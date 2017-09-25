# -*- encoding=UTF-8 -*-
import requests

if __name__ == '__main__':
    try:
        url = "http://m.ip138.com/ip.asp?ip="
        r = requests.get(url + '202.204.80.112')
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.status_code)
        print(r.text[-500:])
    except:
        print("爬取失败！")