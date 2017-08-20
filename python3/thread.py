import threading
import time

class MyThread(threading.Thread):
    def __init__(self, msg):
        threading.Thread.__init__(self) # call parent class constructor
        self.msg = msg
        self.daemon = True
    
    def run(self):
        while True:
            print(self.msg)
            time.sleep(1)

for msg in ["hello", "world"]:
    t = MyThread(msg)
    t.start()
        