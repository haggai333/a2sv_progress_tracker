class Solution(object):
    def maximumSubarraySum(self, nums, k):
        window=set()
        l=0
        result=0
        sumi=0
        for r in range(len(nums)):
            if nums[r] not in window:
                window.add(nums[r])
                sumi+=nums[r]
                if len(window)==k:
                    result=max(result,sumi)
                    window.discard(nums[l])
                    sumi-=nums[l]
                    l+=1
            else:
                while nums[r] in window:
                    window.discard(nums[l])
                    sumi-=nums[l]
                    l+=1
                window.add(nums[r])
                sumi += nums[r]

            
        return result   
        