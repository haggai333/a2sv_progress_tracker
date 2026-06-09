class Solution(object):
    def search(self, nums, target):
        l=0
        r=len(nums)-1
        while r>l:
            mid=(r+l)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[l]:
                if target<nums[mid] and target>=nums[l]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if target<=nums[r] and target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
        if nums[l]==target:
            return l
        return -1




        