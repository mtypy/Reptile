import requests
from lxml import etree


class qiushispider():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        self.base_url = "http://www.qiushibaike.com/8hr/page/{}/"

    def get_url_list(self):
        return [self.base_url.format(page) for page in range(1, 14, 1)]

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.text

    def parse_html(self, html):
        eroot = etree.HTML(html)
        return eroot.xpath('//a[@class="recmd-content"]/text()')

    def save_item(self, item):
        print(item)

    def run(self):
        # 获取url列表
        url_list = self.get_url_list()
        for url in url_list:
            # 发送请求获取html
            html = self.parse_url(url)

            # 3. 从 html 中提取数据
            items = self.parse_html(html)

            # 4. 保存数据
            for item in items:
                self.save_item(item)


if __name__ == '__main__':
    spider = qiushispider()
    spider.run()
