#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 1. 导入模块
import urllib.request
import urllib.parse


wd = input("请输入查询内容:")

# 2. 发送请求获取响应
# 定义请求地址

url = "https://www.baidu.com/s?wd="

# 定义自定义请求头
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

# 定义请求对象
request = urllib.request.Request(
    # 需要对参数进行 url 编码
    # 为什么要进行 url 编码，处理 http 协议中出现关键字符
    url=url + urllib.parse.quote(wd),
    headers=headers
)
print(url + urllib.parse.quote(wd))

# 发送请求
response = urllib.request.urlopen(request)

# 返回是二进制数据
content = response.read()
# 获取字符串
html = content.decode('utf-8')
print(html)
# 3. 处理响应内容
with open('02.html','wb') as f:
    f.write(response.read())