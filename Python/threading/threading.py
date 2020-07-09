from threading import Thread
import time

############ Classthread ############
print('############ Classthread ############')
starttime_classthread = time.time()

class Hello(Thread):
    def __init__(self, breaktime):
        Thread.__init__(self)
        self.breaktime = breaktime

    def run(self):
        for _ in range(5):
            print('Hello')
            time.sleep(self.breaktime)

class Hi(Thread):
    def __init__(self, breaktime):
        Thread.__init__(self)
        self.breaktime = breaktime

    def run(self):
        for _ in range(5):
            print('Hi')
            time.sleep(1)

classthread1 = Hello(1)
classthread2 = Hi(1)

classthread1.start()
time.sleep(0.1)
classthread2.start()

classthread1.join()
classthread2.join()

endtime_classthread = time.time()
difference_classthread = endtime_classthread - starttime_classthread
print('\nProgramm completed in ' + str(round(difference_classthread, 2))+ ' s')
print('############ Classthread ############\n\n#----------------------------------------------------------------#\n')
############ Classthread ############

#----------------------------------------------------------------#

############ Functionthread ############
print('############ Functionthread ############')
starttime_functionthread = time.time()

def hello(breaktime):
    for _ in range(5):
        print('Hello')
        time.sleep(breaktime)

def hi(breaktime):
    for _ in range(5):
        print('Hi')
        time.sleep(breaktime)

functionthread1 = Thread(target=hello, args=[1.5])
functionthread2 = Thread(target=hi, args=[1.5])

functionthread1.start()
time.sleep(0.1)
functionthread2.start()

functionthread1.join()
functionthread2.join()

endtime_functionthread = time.time()
difference_functionthread = endtime_functionthread - starttime_functionthread
print('\nProgramm completed in ' + str(round(difference_functionthread, 2)) + ' s')
print('############ Functionthread ############\n\n#----------------------------------------------------------------#')
############ Functionthread ############

############ Functionthread(increasing global value) ############
print('############ Functionthread(increasing global value) ############')
starttime_functionthread2 = time.time()

value = 0

def increment_value():
    global value
    for i in range(10):
        value = value + 1
        time.sleep(0.1)
        print(value)

incr_thread = Thread(target=increment_value)
incr_thread.start()
incr_thread.join()

print("Read value is: " + str(value))

endtime_functionthread2 = time.time()
difference_functionthread2 = endtime_functionthread2 - starttime_functionthread2
print('\nProgramm completed in ' + str(round(difference_functionthread2, 2)) + ' s')
print('############ Functionthread(increasing global value) ############\n\n#----------------------------------------------------------------#')
############ Functionthread(increasing global value) ############