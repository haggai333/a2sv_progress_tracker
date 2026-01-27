class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        sum=0
        for i in nums:
            sum+=i
        size=len(nums)    
        arthimeticsum=size*(size+1)/2
        if sum==arthimeticsum:
            return int(size)
        else:
            return int(abs(sum-arthimeticsum))
            