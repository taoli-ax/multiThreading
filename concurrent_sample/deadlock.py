
import time
from concurrent.futures import ThreadPoolExecutor

"""
A deadlock is a concurrency failure mode where a process or processes wait for a condition that never occurs. The
result is that the deadlock processes are unable to progress and the program is stuck or frozen and must be
terminated forcefully

"""

"""
github resources
https://github.com/brianquinlan/cpython/blob/4a46adc7746930c4589ee483cad88d3f8504c045/Doc/library/concurrent.futures.rst#L4
"""


def wait_on_b():
    time.sleep(5)
    print(b.result())  # b will never complete because it is waiting on a.
    return 5


def wait_on_a():
    time.sleep(5)
    print(a.result())  # a will never complete because it is waiting on b.
    return 6


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)
