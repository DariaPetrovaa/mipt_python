import multiprocessing
import time
import matplotlib.pyplot as plt
from multiprocessing import Queue,freeze_support
import timeit
import random
import numpy as np


def multiply(c1, c2):
    return np.dot(c1,c2)


def creator(q,res):
    q.put(res)
    return q

a=0

def consumer(q):
    global a
    while not q.empty():
        res = q.get()
        a+=res
    return a


def cut(arr, number):
    res = np.array_split(arr, number)
    for i in res:
        yield i


def run_processes(counter,v1,v2,q):
    freeze_support()
    processes = []
    for new in zip(cut(v1,counter),cut(v2,counter)):
        processes.append(multiprocessing.Process(target=multiply, args = (new[0],new[1])))
    for process in processes:
        process.start()
    start_time = time.time()
    for process in processes:
        process.join()
    #consumer(q)              if we want to see the results
    finish = time.time() - start_time
    return finish

q = Queue()
number_of_processes = [2,4,6,8]
v1 = [random.random() * 10**6 for i in range(2*10**6)]
v2 = [random.random() * 10**6 for i in range(2*10**6)]

time1=[]
time_=[]
for n in number_of_processes:
    for k in range(5):
        finish = run_processes(n,v1,v2,q)
       # print ('Finished. Scalar production is: {}. Runtime is: {}. Number of processes is: {}.'.format(a,round(finish,10),n))
        time1.append(finish)
        a=0
    time_.append(sum(time1)/len(time1))

print(time_)


plt.plot(number_of_processes,time_)
plt.grid(True)
plt.show()

