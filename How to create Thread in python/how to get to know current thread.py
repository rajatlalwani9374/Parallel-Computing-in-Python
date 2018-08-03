import threading
import time

def first_fun():
    print (threading.currentThread().getName()+\
           str(' is starting \n'))
    time.sleep(2)
    print(threading.currentThread().getName()+\
          str(' is exiting\n'))
    return
def second_fun():
    print (threading.currentThread().getName()+\
           str(' is starting \n'))
    time.sleep(2)
    print(threading.currentThread().getName()+\
          str(' is exiting\n'))
    return
def third_fun():
    print (threading.currentThread().getName()+\
           str(' is starting \n'))
    time.sleep(2)
    print(threading.currentThread().getName()+\
          str(' is exiting\n'))
    return
if __name__ == "__main__":

    t1 = threading.Thread\
         (name='first_fun', target=first_fun)
    t2 = threading.Thread\
         (name='second_fun', target=first_fun)
    t3 = threading.Thread\
         (name='third_fun', target=first_fun)

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
