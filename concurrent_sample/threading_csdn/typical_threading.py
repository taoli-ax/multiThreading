import threading
from threading import Thread
import time

start = time.perf_counter()


def process_task(username):
    print(f" {username} start task")
    time.sleep(2)
    print(f"{username} task done \n")


# t1 = threading.Thread(target=process_task, args=())
# t2 = threading.Thread(target=process_task, args=())
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()


# 错误用法 1 等同于顺序运行10次线程
# for _ in range(10):
#     t = threading.Thread(target=process_task, args=())
#     t.start()
#     t.join()

# 错误用法 2
# threads = [threading.Thread(target=process_task, args=()) for _ in range(10)]
# for t in threads:
#     t.start()
#     t.join()

users = ["TaoL","Marco","Antony", "Octavius", "Cleopatra"]
threads = []
for _,name in enumerate(users):

    t = threading.Thread(target=process_task, args=(name,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.perf_counter()

# join()之后才运行
print("cost :", end - start)
