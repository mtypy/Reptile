# 导入模块
import requests

# 下载图片地址
url = "http://pic.rmb.bdstatic.com/f0d15cf31f201fe04c46f078df951655.jpeg"

# 发送获取响应
response = requests.get(url)

# 保存图片
with open("./statics/image1.png", "wb") as f:
    f.write(response.content)
