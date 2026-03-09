class Solution(object):
    def countPairs(self, nums, target):
        count=0
        nums.sort()
        l=0
        r=len(nums)-1
        while r>l:
            if nums[l]+nums[r]<target:
                
                count+=r-l
                l+=1
            else :
                r-=1
    
        return count

        
        