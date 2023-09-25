import time
from concurrent.futures import ThreadPoolExecutor

"""
N threads run at same time
N times : compare with sequential execution, the efficiency is improved by 5 times
"""


def call_api(uri):
    time.sleep(1)
    return {"result":f"{uri} called"}


if __name__ == '__main__':
    stat_time= time.time()

    # resources to be execute
    urls = [
        "www.test1.com",
        "www.test2.com",
        "www.test3.com",
        "www.test4.com",
        "www.test5.com",
    ]

    # create ThreadPoolExecutor instance with 10 workers
    thread_pool = ThreadPoolExecutor(10)

    # create threads pool
    pools = []
    for url in urls:
        # create thread handler
        pool = thread_pool.submit(call_api, (url,))
        # append into thread pool
        pools.append(pool)

    # start thread pool
    for p in pools:
        print(p.result())
    end_time = time.time()

    elapsed = end_time - stat_time
    print(f"Elapsed {elapsed}s")
