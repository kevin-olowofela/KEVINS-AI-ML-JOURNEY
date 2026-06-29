class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h= self.get_hash(key)
        if self.arr[h] is None:
            return None
        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                return self.arr[h][1]
            h = (h + 1) % self.MAX
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        start_index = h  # Remember where we started to detect a full table

        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                self.arr[h] = (key, val)
                return
        
            h = (h + 1) % self.MAX
            if h == start_index:
                raise Exception("Hash table overflow: No available space left.")

        self.arr[h] = (key, val)

        
    def __delitem__(self, key):
        h = self.get_hash(key)
        start_index = h  # Remember where we started to detect a full loop

        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                self.arr[h] = None
                return
            
            h = (h + 1) % self.MAX
            if h == start_index:
                break  # We've looped through the entire table without finding the key


date=HashTable()
date['March 18'] = 100
date['March 7'] = 200
print(date['March 7'])
print(date['March 18'])



