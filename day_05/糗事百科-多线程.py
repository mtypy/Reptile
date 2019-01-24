
from queue import Queue
import requests
from threading import Thread as Task

from lxml import etree
import time


class qiushiSpider():
    def __init__(self):
        self.base_url = "http://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }

        # 添加三个线程
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.item_queue = Queue()

    def get_url_list(self):
        for page in range(1, 14, 1):
            url = self.base_url.format(page)
            self.url_queue.put(url)

    def get_html(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers)
            html = response.text
            self.html_queue.put(html)
            self.url_queue.task_done()

    def get_items(self):
        while True:
            html = self.html_queue.get()
            eroot = etree.HTML(html)
            items = eroot.xpath('//a[@class="recmd-content"]/text()')
            for item in items:
                self.item_queue.put(item)
            self.html_queue.task_done()

    def save_item(self):
        while True:
            item = self.item_queue.get()
            print(item)
            self.item_queue.task_done()

    def run(self):
        tasks = []

        get_url_list_task = Task(target=self.get_url_list)
        tasks.append(get_url_list_task)

        for i in range(0, 5):
            get_html_task = Task(target=self.get_html)
            tasks.append(get_html_task)

        for i in range(0, 3):
            get_items_task = Task(target=self.get_items)
            tasks.append(get_items_task)

        save_item_task = Task(target=self.save_item)
        tasks.append(save_item_task)

        for task in tasks:
            task.setDaemon(True)
            task.start()

        # 保证子线程运行优先于主线程
        time.sleep(1)
        self.url_queue.join()
        self.html_queue.join()
        self.item_queue.join()


if __name__ == '__main__':
    spider = qiushiSpider()
    spider.run()
