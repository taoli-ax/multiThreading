import threading
import time

"""
Youtube resources
https://www.youtube.com/watch?v=A_Z1lgZLSNc
"""

Done = False


def worker():
    counter = 0

    while not Done:
        time.sleep(1)
        counter += 1
        print(counter)


threading.Thread(target=worker, daemon=False).start()

input("user interrupt done to ture")
Done = True
