class Solution(object):
    def runningSum(self, nums):
        answer=[nums[0]]
        for i in range(1,len(nums)):
            answer.append(answer[-1]+nums[i])
        return answer
        