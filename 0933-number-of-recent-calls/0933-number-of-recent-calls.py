class RecentCounter(object):

    def __init__(self):
        self.answer=deque()
        

    def ping(self, t):
        self.answer.append(t)
        while self.answer and not(t-3000<=self.answer[0]<=t):
            self.answer.popleft()
        return len(self.answer)
        


        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)