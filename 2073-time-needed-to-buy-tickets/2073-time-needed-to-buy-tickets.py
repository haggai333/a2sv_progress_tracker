class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        line=deque()
        count=0
        for i in range(len(tickets)):
            line.append(i)
        while tickets[k]>0:
            index=line[0]
            if tickets[index]>=2:
                tickets[index]-=1
                line.popleft()
                line.append(index)
            elif tickets[index]==1:
                tickets[index]-=1
                line.popleft()
            count+=1
        return count
        

        
        