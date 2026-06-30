from collections import deque
import time
import threading

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        if self.is_empty():
            return None
        return self.buffer[-1]
q = Queue()   
def place_order(*args):
    global q
    for order in args:
        q.enqueue(order)
        print(f'placing {order}....')
        time.sleep(0.5)
def serve_order():
    time.sleep(1)
    while not q.is_empty():
        print(f'serving {q.dequeue()}')
        time.sleep(2)

orders = ['pizza','samosa','pasta','biryani','burger']

t1=threading.Thread(target=place_order,args=(orders))
t2=threading.Thread(target=serve_order)
t1.start()
t2.start()
t1.join()
t2.join()