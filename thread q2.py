from threading import *
import time
def num():
    for i in range(1,11):
        print(i)
        time.sleep(1)

t=Thread(target=num)
t.start()
