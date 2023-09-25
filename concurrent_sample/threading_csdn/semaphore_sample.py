"""
csdn resources
https://www.cnblogs.com/renpingsheng/p/7202818.html

信号量 决定了同时有几个线程可以工作
"""

import time
import threading

s1 = threading.Semaphore(5)  # 添加一个计数器


def foo():
    s1.acquire()  # 计数器获得锁
    time.sleep(2)  # 程序休眠2秒
    print("ok", time.ctime())
    s1.release()  # 计数器释放锁


for i in range(20):
    t1 = threading.Thread(target=foo, args=())  # 创建线程
    t1.start()  # 启动线程
