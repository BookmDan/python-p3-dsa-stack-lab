class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(item)
        else:
            return None

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.limit is not None and len(self.items) == self.limit


    def search(self, target):
        try:
            index = self.items.index(target)
            return len(self.items) - 1 - index
        except ValueError:
            return -1
