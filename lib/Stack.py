class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else: 
            return False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.insert(len(self.items), item)
            return self.items

    def pop(self):
        if len(self.items) >= 1:
            return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) >= self.limit:
            return True
        else: 
            return False

    def search(self, target):
        list = self.items[::-1]
        if target in list:
            return list.index(target)
        else: 
            return -1
        
    
hi = Stack([1,2,3,4,5])
print(hi.search(2))