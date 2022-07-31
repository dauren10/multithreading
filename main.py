import time
import threading

def get_data(data):
    while True:
        print(f"[{threading.currentThread().name}]-{data}")
        time.sleep(1)

thr=threading.Thread(target=get_data,args=(str(time.time()),),name="the-1")
thr.start()

for i in range(100):
    print(f"current {i}")
    time.sleep(1)

    if i % 10 == 0:
        print(threading.active_count())
        print(threading.enumerate())
        print(thr.is_alive())