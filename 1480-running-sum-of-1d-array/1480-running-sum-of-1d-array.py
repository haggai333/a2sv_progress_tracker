class Solution(object):
    def runningSum(self, nums):
        answer=[]
        sum=0
        for i in nums:
            sum+=i
            answer.append(sum)
        return answer
        