class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x,y=-1,-1
        l=0
        r=len(nums)-1
        while r>=l:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid
                l=mid
                break
        if r>=l:
            while l>0 and nums[l-1]==target:
                l-=1
            while r<len(nums)-1 and nums[r+1]==target:
                r+=1
        else:
            return [-1,-1]
            
        return [l,r]
        

        