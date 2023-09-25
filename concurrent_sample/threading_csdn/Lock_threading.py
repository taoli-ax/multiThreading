import time
from threading import Lock
import threading
"""
csdn resource
https://blog.csdn.net/xiaoyu_wu/article/details/102815302
"""


total = 0
lock = Lock()


def add():
    global lock
    global total
    for i in range(100):
        lock.acquire()  # 上锁
        total += 1

        lock.release()  # 解锁


def desc():
    global lock
    global total
    for i in range(100):
        lock.acquire()  # 上锁
        total -= 1
        # print(f"desc:{total}")
        lock.release()  # 解锁

start_time= time.time()
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

# thread1.join()
# thread2.join()
print(f" {total}")
print(f"elapse time : { time.time()- start_time} ")