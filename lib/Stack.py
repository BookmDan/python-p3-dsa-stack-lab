class Stack:

    def __init__(self, items = [], limit = 100):
        pass

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.limit is not None and len(self.items) == self.limit


    def search(self, target):
        try:
            index = self.items.index(value)
            return len(self.items) - 1 - index
        except ValueError:
            return -1
