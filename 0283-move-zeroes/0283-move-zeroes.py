class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0
        r=0
        size=len(nums)
        if size<2:
            return 
        while r<size:
            if nums[l]!=0:
                l+=1
                r+=1
            if nums[r]!=0:
                nums[r],nums[l]=nums[l],nums[r]
                r+=1
                l+=1
            else:
                r+=1
            
        