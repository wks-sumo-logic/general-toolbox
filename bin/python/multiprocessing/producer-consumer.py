#!/usr/bin/env pyathon3 

import multiprocessing 
import time
import os

q = multiprocessing.JoinableQueue()

def producer():
    for item in range(30):
        time.sleep(2)
        q.put(item)
    pid = os.getpid()
    print(f'producer {pid} done')


def worker():
    while True:
        item = q.get()
        pid = os.getpid()
        print(f'pid {pid} Working on {item}')
        print(f'pid {pid} Finished {item}')
        q.task_done()

for i in range(5):
    p = multiprocessing.Process(target=worker, daemon=True).start()

producers = []
# it is easy to extend it to multi producers.
for i in range(1):
    p = multiprocessing.Process(target=producer)
    producers.append(p)
    p.start()

# make sure producers done
for p in producers:
    p.join()

# block until all workers are done
q.join()
print('All work completed')


