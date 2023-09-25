"""
Github resources
https://github.com/brianquinlan/cpython/blob/4a46adc7746930c4589ee483cad88d3f8504c045/Doc/library/concurrent.futures.rst#L4
"""

import concurrent.futures
import time
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']


# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    # print(f"{url},{timeout}")
    time.sleep(1)
    return f"{url} done"
    # with urllib.request.urlopen(url, timeout=timeout) as conn:
    #     return conn.read()


# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    print(future_to_url)
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
