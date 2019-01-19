"""
分析
url
    https://movie.douban.com/j/search_subjects

请求方式
    GET

请求参数
    "type": "movie",
    "tag": "热门",
    "sort": "recommend"
    "page_limit": "20",
    "page_start": "20",

请求头
User-Agent: Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36

"""

import requests
import  json
# 定义请求的url

url = "https://movie.douban.com/j/search_subjects"

# 自定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

for page_start in range(0, 100, 20):
    # 参数
    params = {
        "type": "movie",
        "tag": "热门",
        "sort": "recommend",
        "page_limit": "20",
        "page_start": page_start   # 起始页
    }

    # 发送get请求参数
    response = requests.get(
        url=url,
        params=params
    )

    # 返回二进制数据
    content = response.content  # 返回二进制类型

    # # 方式一
    # # 直接通过content decode 获取
    # html = content.decode("utf-8")
    # # print(html)
    # result = json.loads(html)

    # # 方式二
    # response.encoding = "utf-8"
    # html = response.text
    # result = json.loads(html)

    # 方式三
    # 解码转成html数据
    result = response.json()  # json.loads(html)

    if len(result["subjects"]) == 0:
        break

    for movie in result["subjects"]:

        print(movie["title"], ":", movie["rate"])
