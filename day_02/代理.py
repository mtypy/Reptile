# 导入模块
import requests

# 定义请求地址
url = "http://www.baidu.com"

# 自定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

# 定义代理服务器
proxies = {
    # "http": "http://IP地址:端口号",
    # "https": "https://IP地址:端口号"
    "http": "http://119.101.112.6:9999"
}


response = requests.get(url, headers=headers, proxies=proxies)

# 获取响应的html内容
html = response.text
print(html)
