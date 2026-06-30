from collections import deque

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


def generate_binary_numbers(n):
    q = Queue()
    q.enqueue("1")
    for _ in range(n):
        current = q.front()
        print(current)
        q.dequeue()
        q.enqueue(current + "0")
        q.enqueue(current + "1")

generate_binary_numbers(15)
