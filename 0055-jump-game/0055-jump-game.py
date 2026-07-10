class Solution(object):
    def canJump(self, nums):
        if len(nums)<=1:
            return True
        if nums and nums[0]==0:
            return False
        i=0
        furthest=0
        while i<len(nums)-1:
            if furthest<i:
                return False
            for j in range(i,i+nums[i]):
                if j<len(nums)-1:
                    if furthest<j+nums[j]:
                        furthest=j+nums[j]
                else:
                    return True
            i+=1
        return furthest>=len(nums)-1



        