"""
分析
url
    http://tieba.baidu.com/f

请求方式
GET

请求参数
    kw: python  贴吧名称
    ie: utf-8
    pn: 50      表示页数 从 0 开始每页 50 递增，最大 44100

请求头
User-Agent
"""
import requests


class TiebaSpider():
    def __init__(self, kw, max_pn=50):
        # 定义请求的url
        self.kw = kw
        self.max_pn = max_pn
        self.url_base = "http://tieba.baidu.com/f"

        # 自定义请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }

    # #  获取url列表
    def get_url_list(self):
        # url_list = []
        # for pn in range(0, self.max_pn, 50):
        #     url = self.url_base.format(self.kw, pn)
        #     url_list.append(url)
        # return url_list
        return [self.url_base.format(self.kw, pn) for pn in range(0, self.max_pn, 50)]

    def get_html(self, url):
        response = requests.get(
            url=url,
            headers=self.headers
        )
        return response.text

    def get_data(self, html):
        return html

    def save_data(self, data):
        print(data)

    def run(self):
        # 1.获取url列表
        url_list = self.get_url_list()
        for url in url_list:

            # 2.发送请求获取响应
            html = self.get_html(url)

            # 3.从html中提取数据
            data = self.get_data(html)

            # 4. 保存数据
            self.save_data(data)


if __name__ == '__main__':
    Tieba = TiebaSpider("python", max_pn=44100)
    Tieba.run()
