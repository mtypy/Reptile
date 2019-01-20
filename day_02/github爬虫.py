"""
# 方法一
# 通过已经登陆的cookie进行爬取

# 导入模块
import requests

# 发起请求 获取响应
url = "https://github.com/login"

# 自定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Cookie": "_ga=GA1.2.282767259.1547109646; _octo=GH1.1.903461036.1547109666; has_recent_activity=1; tz=Asia%2FShanghai; logged_in=no; _gh_sess=d1VDZkQyYkJmdjVFdUxUL1ZFSUE4cUE5SW40RVZoZC9OUWxZOEw5d2ljbG9XVjVkc2dVcE5hU1luVG1YdmFQUjhjSzFFQUhmNFM2YUlOcERSa3ppbTNHNTJ1dHB3WHVRQzZrVmJkd0NBbzYxMWVGRnJRU2xSRk45ZEJ6YXViUEhMU3MzN01Hc1JUN1d5aGxXQXV0Rm9FQlpvOUJCZTZ2ZGxIWnRMc1krcjdKTnVjcERyMTZSdFNKTE84OGd5UHQ1MGI5aDJHZU5Hc0JCVUZvYlVlbi9VNkRZcXFKOUZQZHhtQVUzNXBadDBpTllSblRJdE1NSDNpeFNGWVhKVTJ5N2d3V2grY2F2RWFDVFJoSjllSURlY0xVR1JEaXJLa2c3OFU5VjdWTHNrcWd6NzNYa2J0c3JqTHpHZTM4MmphL1JOZDRPWEtwRlo1djJYamx5NlU0REdsRzRSQ3FUYXNIaHQrUGRFYTd2OEtQS1Z3N0xmTTZZN2RhZFNSSHFHWlY2bDFWekgvUXVycGhiSUhDR3N2Q1NnbGFJbXcyaXdNREJYTXlFOVYyOFh5aFJiUFpWUFpsZFlkVnB4UmFXc3Q4UC0tbHozay9xK3ZBbGFQODd4cmpwT0piUT09--38770ade9a335c7009931c517abd4380557e5aa0"
}

response = requests.get(
    url,
    headers=headers
)

# 获取响应的内容 返回的是byte
content = response.content

with open("../statics/github.html", "wb") as f:
    f.write(content)

"""

# 方法二
# 模拟登陆获取cookie 进行爬去
# 导入模块
import requests

# 登陆获取cookie
url = "https://github.com/session"

data = {
"commit": "Sign in",
"utf8": "✓",
"authenticity_token": "ng7vM1Zl1CVgO7Pd/9e0KrQVBaWLNRCG7mhe22+tOFQnF/wjxF39z6/GNGw6939B0BWaDREhoYl7kjsUDrpMhw==",
"login": "mty_22968712@163.com",
"password": "ming7642537"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Cookies": "ga=GA1.2.282767259.1547109646; _octo=GH1.1.903461036.1547109666; has_recent_activity=1; tz=Asia%2FShanghai; _gat=1; logged_in=no; _gh_sess=MCswQS94U2lqZERlZkV6QXRqcEljWjF4L1FlZGEwcng3NjdWY1JTeDI0UXI0Mjk0TVlsVUtmUktkK2VmTno1QWJjRkMwWFR0cWM1dFBvbnJ5L05peDZOSm92RlNDd0dwRW1ESk9SMGtBV1JkNCtoeHlvclh0ek5veVBTVWs4TjRhR2xnYU44cWRCdHhQVmxZSHpvUVFTQWFZTTlqczFYV3l2TXk1SDQ1cHZxb1hJbmdQajFlTWpZUzRLNThTSjNocHBLZ3VDVWJmL1BLT0xLMDVLNzBHSklCMG9OY3lkWWRjZC9NemZkdnlES3ZzMkorcU9mVVQ0cmd3aFRYVVkzNE11QnFsc29ucVBRbHMya1Y5NWlEbmo5RUkzZlZjZ0ZYUDhzWjZCUjdmck13L1ZKRm4xQm9qYkRzWCtsdXNkcmFMSTFMN2VUVDhKZDBlU2pEVDVnek5XRmpER0JUeGR0RjBDZGFjMGR3RmloUDE2aTN6dXozVUhNQUhPNi94bUVMRE8zSWhJT2lVOHFwZmNLNnIxNXc3S3FWekx6eDkxc3hXK3h2NjVlUlZ1UT0tLVRKdDNJNDZzSk9mYmxnSUpWazRwTEE9PQ%3D%3D--999d30162fb4af94642a210001ed5b9b90746bba",
    "Referer": "https://github.com/login"

}

response = requests.post(
    url=url,
    headers=headers,
    data=data
)

# 获取登陆成功后的cookie
cookies = response.cookies
print(cookies)

url = "https://github.com/"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }, cookies=cookies
)

# 获取响应的内容 返回的是byte
content = response.content

with open("../statics/github1.html", "wb") as f:
    f.write(content)
