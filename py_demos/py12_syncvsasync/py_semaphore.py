import threading
import time
from py_mod import st_code, st_markline, code_print
import streamlit as st

### StartofFunc###

def py_semaphore():
    # read obsidian Streamlit Threading Issue
    def pysemaphore():
        class simple_semaphore:
            def __init__(self, max_num):
                self.max = max_num
                self.lock = threading.Lock()
                self.count  = 0
            def acquire(self):
                while True:
                    with self.lock:
                        if self.count < self.max:
                            self.count += 1
                            return
                time.sleep(0.01)
            def release(self):
                with self.lock:
                    self.count -= 1
        def work(sema, idx):
            sema.acquire()
            print(f"task {idx} start to run")
            #st.code(f"task {idx} start to run")
            time.sleep(0.3)
            sema.release()
        sem = simple_semaphore(2)
        for i in range(6):
            threading.Thread(target=work,args=(sem,i)).start()
    #pysemaphore()
#py_semaphore()
### EndofCodeSection###
