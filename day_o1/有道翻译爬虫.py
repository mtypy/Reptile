'''

需求：输入一个英文单词，返回一个翻译结果

https://fanyi.baidu.com/basetrans

POST

请求参数

query: what

from: en

to: zh

请求头

User-Agent： Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1

'''

'''

sign 随着 query  变化而变化

1. 尽量不碰下面2种方案就不碰下面两种方案（切换手机h5端）
2. 模拟仿真浏览器(selenium) （爬虫底线）（出数据缓慢无比）
3. 查看js源码找到 query 和 sign 对应关系（爬虫最高进阶，js逆向）（极快）

'''

import requests

url = "https://fanyi.baidu.com/basetrans"

query = input("请输入单词:")

data = {

    "from": "en",
    "to": "zh",
    "query": query

}

headers = {

    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",

}

response = requests.post(url, headers=headers, data=data)

print(response.json()["trans"][0]["dst"])
