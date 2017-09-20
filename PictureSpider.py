import requests

if __name__ == '__main__':
    path = "D:/abc.jpg"
    url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
    r = requests.get(url)
    print(r.status_code)
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()