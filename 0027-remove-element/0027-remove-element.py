class Solution(object):
    def removeElement(self, nums, val):
        l=0
        while   l< len(nums):
            if nums[l]==val:
                nums[-1],nums[l]=nums[l],nums[-1]
                
                nums.pop()
                continue
                
                
            l+=1
        print(nums)
        