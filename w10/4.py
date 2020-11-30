from threading import Thread
import subprocess
from queue import Queue
import time
queue = Queue()
hosts = ["ya.ru", "rambler.ru", "mail.ru", "google.com"]
def pinger(i, q):
    time.sleep(i)
    host = q.get()
    print ("%s: Пингуем %s" % (i, host))
    ret = subprocess.call("ping -c 1 %s" % host,
                        shell=True,
                        stdout=open('/dev/null', 'w'),
                        stderr=subprocess.STDOUT)
    if ret == 0:
        print ("%s передает привет" % host)
    else:
        print ("%s не отвечает" % host)
    q.task_done()
for i in range(1, len(hosts)+1):
    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()
    
for host in hosts:
    queue.put(host)
time.sleep(10)
queue.join()

