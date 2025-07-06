"""
为什么会使用 httpx？
因为有些网站的协议是强制：http2.0 协议
requests urllib 这些包都只能处理 http1.1协议的网站
"""
from math import trunc

import requests

import httpx

if __name__ == '__main__':
    # 下面这3行代码会报错，说是 RemoteDisconnected 错误
    # url = 'https://spa16.scrape.center/'
    # resp = requests.get(url)
    # print(resp.text)

# httpx 的使用和 requests 没什么本质区别
#     url = 'https://www.httpbin.org/get'
#     headers = {
#         'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10_15_7)AppleWebKit/537.36(KHTML,likeGecko)Chrome/90.0.4430.93Safari/537.36'
#     }
#     resp = httpx.get(url, headers=headers)
#     print(resp.status_code)
#     print(resp.headers)
#     print(resp.text)

# 使用 http2.0 请求网站
    client = httpx.Client(http2=True)
    resp = client.get('https://spa16.scrape.center/')
    print(resp.text)

    pass