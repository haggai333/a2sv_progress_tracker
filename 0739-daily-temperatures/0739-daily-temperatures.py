class Solution(object):
    def dailyTemperatures(self, temperatures):
        next={}
        line=deque()
        answer=[]
        for index,i in enumerate(temperatures):
            while len(line)>0 and temperatures[line[-1]]<i:
                next[line[-1]]=index
                line.pop()
            line.append(index)
        for i in range(len(temperatures)):
            if i in next:
                answer.append(next[i]-i)
            else:
                answer.append(0)
        return answer
        
        
        