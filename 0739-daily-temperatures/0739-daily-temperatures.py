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
            a=next.get(i,0)
            if a!=0:
                answer.append(a-i)
            else:
                answer.append(0)
        return answer
        
        
        