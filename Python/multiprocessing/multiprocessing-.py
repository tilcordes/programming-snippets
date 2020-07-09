import multiprocessing
import math
import time

start_time = time.time()

def factorize(num):
    res = []
    i = 2
    while True:
        if num == 1:
            return res
        rest = num % i
        if rest == 0:
            res.append(i)
            num = num / i
        else:
            i = i+1
    
def worker(queue, numbers):
    result = {}
    for i in numbers:
        result[i] = factorize(i)
        queue.put(result)

def factor(numbers, processes):
    queue = multiprocessing.Queue()
    chunks = int(math.ceil(len(numbers) / processes))
    procs = []
    for i in range(processes):
        proc = multiprocessing.Process(target=worker, args=(queue, numbers[chunks*i:chunks*(i+1)]))
        procs.append(proc)
        proc.start()

    results = {}
    for i in range((len(numbers))):
        results.update(queue.get())

    for i in procs:
        i.join()
    return results

if __name__ == '__main__':
    res = factor([1000, 2384724, 73495, 8420938], 4)
    print(res)
    end_time = time.time()
    print(str(round(end_time-start_time, 2)) + ' s')