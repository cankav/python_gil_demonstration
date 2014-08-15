import psutil
import threading
from multiprocessing import Process

stop=False

def busy_func():
    while not stop:
        pass

def print_cpu_usage(n, msg):
    print msg
    for i in range(n):
        print psutil.cpu_percent(interval=1, percpu=True)

processes = []

def start_paralel(t):
    print "starting", t
    for i in range(8):
        if t == 'threads':
            thr = threading.Thread(target=busy_func)
            thr.start()
        else:
            p = Process(target=busy_func)
            processes.append(p)
            p.start()

    print "done"
        

print_cpu_usage(10, "before starting threads (idle)")
start_paralel('threads')
print_cpu_usage(10, "threads running")
stop = True

print_cpu_usage(10, "after threads stopped (idle)")
stop = False
start_paralel('processes')
print_cpu_usage(10, "processes running")

for i in range(len(processes)):
    processes[i].terminate()

