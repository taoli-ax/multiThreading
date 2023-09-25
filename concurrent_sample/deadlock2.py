from concurrent.futures import ThreadPoolExecutor

"""
github resources
https://github.com/brianquinlan/cpython/blob/4a46adc7746930c4589ee483cad88d3f8504c045/Doc/library/concurrent.futures.rst#L4
"""
def wait_on_future():
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    print(f.result())


executor = ThreadPoolExecutor(max_workers=1)
executor.submit(wait_on_future)
