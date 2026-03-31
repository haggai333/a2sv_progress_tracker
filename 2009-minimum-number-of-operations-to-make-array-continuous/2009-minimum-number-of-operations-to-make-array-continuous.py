class Solution(object):
    def minOperations(self, nums):
        size=len(nums)
        nums=sorted(set(nums))
        answer=size
        r=0
        for l in range(len(nums)):
            while r<len(nums) and nums[r]<nums[l] + size:
                r+=1
            answer=min(answer,size-(r-l))
        return answer
        

        
        