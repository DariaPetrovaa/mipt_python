import multiprocessing
import time
import matplotlib.pyplot as plt
from multiprocessing import Queue
import timeit

def multiply(c1, c2):
    return c1*c2

def creator(q,res):
    q.put(res)
    return q

a=0

def consumer(q,counter):
    global a
    for i in range(counter):
        res = q.get()
        a+=res
    return a    

def run_processes(counter,v1,v2,q):
    processes = [multiprocessing.Process(target=creator, args = (q,multiply(v1[i],v2[i]))) for i in range(0,counter)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    consumer(q,counter)

q = Queue() 
v1 = [1,2,3,5,1,5]
v2 = [33,4,5,44,7,6]
n = len(v1)
start_time = time.time()
run_processes(n,v1,v2,q)
finish = time.time() - start_time
print ('Finished. Scalar production is: {}. Runtime is: {}.'.format(a,round(finish,10)))

def scalar(v1,v2):
    b=0
    for i in range(len(v1)):
        res = v1[i]*v2[i]
        b+=res
    return b

number_of_processes = [1,1,1,3,3,3]
time1=[]
for k in range(3):
    start_time = timeit.default_timer()
    scalar(v1,v2)
    finish = timeit.default_timer() - start_time
    time1.append(finish)
for k in range(3):
    start_time = time.time()
    run_processes(n,v1,v2,q)
    finish = time.time() - start_time
    time1.append(finish)

#print(time1)

plt.plot(time1,number_of_processes)
plt.grid(True)
plt.show()

