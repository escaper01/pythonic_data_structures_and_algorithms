class MyStack:
    # my own way to implement a stack
    def __init__(self):
        self.items = []
    
    def push(self,elem):
        self.items.append(elem)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items == []:
            return None
        return self.items[-1]

    def is_empty(self):
        if self.items == []:
            return True
        return False

    def get_elements(self):
        return self.items

        