class Solution(object):
    def canJump(self, nums):
        i=0
        furthest=0
        while i<len(nums)-1:
            if furthest<i:
                return False
            if furthest<i+nums[i]:
                furthest=i+nums[i] 
            i+=1
        return furthest>=len(nums)-1



        