from threading import Thread
from time import sleep

class rajat(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = "Hello Rajat\n"

    def print_message(self):
            print(self.message)

    def run(self):
            print("thread starting \n")
            x=0
            while(x<10):
                self.print_message()
                sleep(2)
                x += 1
            print ("thread ended \n")
print ("process started")

hello_python = rajat()
hello_python.start()
print("process ended")
