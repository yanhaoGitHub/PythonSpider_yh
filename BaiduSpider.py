import requests

if __name__ == '__main__':
    kv = {'wd':'Python'}
    r = requests.get("http://www.baidu.com/s",params=kv)
    print(r.status_code)
    print(r.request.url)
    print(len(r.text))