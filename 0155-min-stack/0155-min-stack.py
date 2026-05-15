class MinStack(object):

    def __init__(self):
        self.min=[]
        self.stack=[]
        

    def push(self, val):
        self.stack.append(val)
        if (self.min and val<=self.min[-1]) or not self.min:
            self.min.append(val)
        

    def pop(self):
        if self.min and self.stack[-1]==self.min[-1]:
            self.min.pop()
        return self.stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        if self.min:
            return self.min[-1]
        else:
            return None
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()