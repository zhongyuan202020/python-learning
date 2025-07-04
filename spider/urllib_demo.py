from urllib import request
from urllib import error
from urllib import parse

import ssl
import gzip

"""
这是一个不验证ssl证书的上下文
"""
ssl_context = ssl._create_unverified_context()


def urlopen_get(url):
    """
    基本的 get 请求，获取到响应内容
    1.在使用 urllib 的时候，有的内容需要手动解压缩。
    2.需要一步步去根据返回的header里面，解析到对应的压缩方式，以及编码方式
    :param url: 目标网址
    """
    response = request.urlopen(url, context=ssl_context)
    print('response type:', type(response))
    print('response status:', response.status)
    print('response headers:', response.getheaders())
    print('---------------------------------------')
    headers = response.getheaders()
    content = response.read()
    content_encoding = None
    for header in headers:
        print(header)
        if header[0] == 'content-encoding':
            content_encoding = header[1]
            break
    if content_encoding == 'gzip':
        content = gzip.decompress(content)
    decoded_content = content.decode('utf-8')
    print(decoded_content)


def urlopen_post(url, data):
    """
    post请求方式：
    1. data 是参数，参数需要使用 bytes进行转化。
    :param url: 请求目标
    :param data: 参数
    :return:
    """

    body = bytes(parse.urlencode(data), encoding='utf-8')
    response = request.urlopen(url, body, context=ssl_context)
    print(response.read().decode('utf-8'))


def use_Request_demo(url):
    """
    urlopen可以处理最基本的请求，但是如果要添加header等信息，那么就搞不定了。
    需要使用 Request 类，来达成目的
    :return:
    """
    headers = {
        'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT',
        'Host':'www.httpbin.org'
    }
    dict = {
        'name':'zhangsan'
    }

    body = bytes(parse.urlencode(dict),encoding='utf-8')
    req = request.Request(url,data=body,headers=headers,method='POST')
    resp = request.urlopen(req,context=ssl_context)
    print(resp.read().decode('utf-8'))

def use_handler_opener():
    """
    要补充一点，现在所有的https的url，都必须使用ssl context
    handler中可以有一个httpshander可以使用
    :return:
    """
    username = 'admin'
    password = 'admin'
    url = 'https://ssr3.scrape.center/'

    p = request.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None,url,username,password)
    auth_handler = request.HTTPBasicAuthHandler(p)


    # 构建 httpshandler
    https_handler = request.HTTPSHandler(context=ssl_context)

    opener = request.build_opener(auth_handler,https_handler)

    try:
        resp = opener.open(url)
        html = resp.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        print(e.reason)

def use_proxy_handler():
    proxy_handler = request.ProxyHandler({
        'http':'http://127.0.0.1:7890',
        'https':'https://127.0.0.1:7890',
    })

    https_handler = request.HTTPSHandler(context=ssl_context)
    opener = request.build_opener(proxy_handler,https_handler)
    try:
        response = opener.open('https://www.baidu.com')
        print(response.read().decode('utf-8'))
    except error.URLError as e:
        print(e.reason)



if __name__ == '__main__':
    # urlopen_get('https://www.python.org')
    # urlopen_post('https://www.httpbin.org/post',{'name':'zhangsan'})
    # use_Request_demo('https://www.httpbin.org/post')
    # use_handler_opener()
    use_proxy_handler()