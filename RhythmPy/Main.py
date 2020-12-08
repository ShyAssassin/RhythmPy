import threading 
import time 
  
def thread_foo(stop):
    while True: 
        print("THREAD STILL RUNNING!") 
        if exit_flag: 
            break
exit_flag = False
t = threading.Thread(target = thread_foo, args =(lambda : exit_flag, )) 
t.start() 
time.sleep(0.1) 
print('Done sleeping! Time to stop the threads.')
exit_flag = True
t.join() 
print('THREAD TERMINATED!')