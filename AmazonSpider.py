import requests
if __name__ == '__main__':
    #r = requests.get("https://www.amazon.cn/gp/product/B01M8L5Z3Y")
    #print(r.status_code)
    #print(r.encoding)
    #r.encoding = r.apparent_encoding
    #print(r.text)

    kv = {'user-agent':'Mozilla/5.0'}
    url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
    r = requests.get(url,headers=kv)
    print(r.status_code)
    print(r.request.headers)
    print(r.text)
