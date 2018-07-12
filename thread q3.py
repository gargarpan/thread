from threading import *
import time
def list():
    list=[1,2,3,4,5]
    for i in range(len(list)):
        print(list[i])
        x=2*list[i]
        time.sleep(x)

t=Thread(target=list)
t.start()
