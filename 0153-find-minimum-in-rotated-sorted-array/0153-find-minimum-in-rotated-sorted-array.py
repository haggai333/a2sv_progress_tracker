class Solution(object):
    def findMin(self, nums):
        l=0
        r=len(nums)-1
        while r>l:
            mid=(r+l)//2
            if nums[r]<nums[mid]:
                l=mid+1
            if nums[r]>nums[mid]:
                r=mid
            
            
            
                
            
        return nums[l]
                
        