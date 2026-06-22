class Solution(object):
    def maxNumberOfBalloons(self, text):
        counter=Counter(text)
        answer=float('inf')
        for i in "ballon":
            if i=="l" or i=='o':
                 answer=min(answer,counter.get(i,0)//2)
                 continue

            answer=min(answer,counter.get(i,0))
        return answer