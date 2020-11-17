import threading
import time
import matplotlib.pyplot as plt
#from numpy import dot

#for task 5

a=0
def multiply(c1, c2):
    global a
    res = c1*c2
    lock.acquire()
    a+=res
    lock.release()

def run_threads(counter,v1,v2):
    threads = [threading.Thread(target=multiply, args = (v1[i],v2[i])) for i in range(0,counter)]
    for thread in threads:
        thread.start()

lock = threading.Lock()
v1 = [111111122324355,222456774,333,333574333,134386575859685,55789775463425]
v2 = [3336675346,433787654,533967344658676645444,33367644,777763367,652307563252749573355]
n = len(v1)
start_time = time.time()
run_threads(n,v1,v2)
finish = time.time() - start_time
print ('Finished. Scalar production is: {}. Runtime is: {}.'.format(a,round(finish,10)))

#for task 6

def scalar(v1,v2):
    a=0
    for i in range(len(v1)):
        res = v1[i]*v2[i]
        a+=res
    return a

number_of_threads = [1,1,1,3,3,3]
time1=[]
for k in range(3):
    start_time1 = time.time()
    scalar(v1,v2)
    finish1 = time.time() - start_time1
    time1.append(finish1)
for k in range(3):
    start_time = time.time()
    run_threads(n,v1,v2)
    finish = time.time() - start_time
    time1.append(finish)

print(time1)

plt.plot(time1,number_of_threads)
plt.grid(True)
plt.show()
#runtime increased with the increase of number of threads
