# 线程的基本实现
"""
import threading
import time


def task():
    print("子线程运行")
    time.sleep(3)
    print("子线程运行结束")


th = threading.Thread(target=task)

# 添加守护子线程 如果设置子线程为守护线程，当主线程结束时不管守护线程是否结束都会自动结束
th.setDaemon(True)
th.start()

print("主线程执行结束")
"""

# 队列的基本实现
# 导入模块
from queue import Queue

q = Queue(maxsize=100)
print("qsize", q.qsize())
print("unfinished_task", q.unfinished_tasks)
print("*" * 100)

q.put("abc")
print("qsize:", q.qsize())
print("unfinished_task", q.unfinished_tasks)
print("*" * 100)

q.get()
print("qsize:", q.qsize())
print("unfinished_task", q.unfinished_tasks)
print("*" * 100)

q.task_done()
print("qsize:", q.qsize())
print("unfinished_task", q.unfinished_tasks)
print("*" * 100)

q.join()
print("程序结束")