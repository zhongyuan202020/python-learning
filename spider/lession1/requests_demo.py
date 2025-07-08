import requests

def get_demo1(url):
    r = requests.get(url)
    print(type(r))
    print(r.status_code)
    print(type(r.text))
    print(r.text[:100])
    print(r.cookies)

def get_with_param(url, params):
    r = requests.get(url, params)
    # r.text 是 string 类型的，但是是个 json 格式的字符串
    print(r.text)
    # 可以转成json进行输出
    print(r.json())
    print(type(r.json()))

if __name__ == '__main__':
    # get_demo1('https://www.baidu.com')
    get_with_param('https://www.httpbin.org/get', {'name':'zhangsan','age':25})
    pass