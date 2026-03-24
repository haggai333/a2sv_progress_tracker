class Solution(object):
    def threeSumClosest(self, nums, target):
        answer=0
        close=9999999
        nums.sort()
        
        for r in range(len(nums)):
            l=r+1
            
            ri=len(nums)-1

            while ri>l:
                if abs(target-(nums[ri]+nums[l]+nums[r]))<close:
                    answer=nums[r]+nums[l]+nums[ri]
                    close=abs(target-answer)
                    
                    
                if nums[ri]+nums[l]+nums[r]>target:
                    ri-=1
                else:
                    l+=1
               
        return answer
        
        