class RecentCounter(object):

    def __init__(self):
        self.queue=[]
    def ping(self, t):
        
        self.queue.append(t)
        diff=t-3000
        while len(self.queue)>0 and self.queue[0]<diff:
            self.queue.pop(0)
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)