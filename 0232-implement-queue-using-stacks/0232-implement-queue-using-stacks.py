class MyQueue(object):
    def __init__(self):
        self.queue=list()
        

    def push(self, x):
        print(x)
        temp=list()
        while self.queue:
            a=self.queue.pop()
            temp.append(a)
        temp.append(x)
        print(temp)
        while temp:
            a=temp.pop()
            self.queue.append(a)
        print(self.queue)
        
    def pop(self):
        return self.queue.pop()
        
        

    def peek(self):
        return self.queue[-1]
        

    def empty(self):
        return len(self.queue)==0
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()