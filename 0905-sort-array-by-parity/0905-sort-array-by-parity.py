class Solution(object):
    def sortArrayByParity(self, nums):
        answer=[]
        odds=[]
        for i in nums:
            if i%2==0:
                answer.append(i)
            else:
                odds.append(i)
        return answer+odds
        
        