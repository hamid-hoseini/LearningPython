class Stack():
    
    def __init__(self):
        self.list_stack = []
        
    def is_empty(self):
        if not self.list_stack:
            return True
        else:
            return False
        
    def push(self,item):
        self.list_stack.append(item)
        
    def pop(self):
        return self.list_stack.pop()
    
    def peek(self):
        
        if self.is_empty():
            return None
        else:
            return self.list_stack[-1]
        
    def __repr__(self):
        return repr(self.list_stack)

new_stack = Stack()
new_stack.is_empty()
new_stack.push(4)
print(new_stack.peek())
