class Solution(object):
    def canJump(self, nums):
        furthest=0
        for i in range(len(nums)-1):
            if furthest<i:
                return False
            if furthest<i+nums[i]:
                furthest=i+nums[i] 
        return furthest>=len(nums)-1



        