from threading import *
import time
def message():
    time.sleep(5)
    print("This Is Your Message.. After Sleeping for 5Sec....")

t=Thread(target=message)
t.start()
