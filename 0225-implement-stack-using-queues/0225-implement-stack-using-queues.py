class MyStack(object):

    def __init__(self):
        self.input=deque()
        self.output=deque()
        

    def push(self, x):
        if not self.output:
            self.output.append(x)
            while self.input:
                self.output.append(self.input.popleft())
        else:
            self.input.append(x)
            while self.output:
                self.input.append(self.output.popleft())
        
    def pop(self):
        if self.input:
            return self.input.popleft()
        else:
            return self.output.popleft()        
        

    def top(self):
        if self.input:
            return self.input[0]
        else:
            return self.output[0]
        

    def empty(self):
        if not (self.input or self.output):
            return True
        else:
            return False
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()