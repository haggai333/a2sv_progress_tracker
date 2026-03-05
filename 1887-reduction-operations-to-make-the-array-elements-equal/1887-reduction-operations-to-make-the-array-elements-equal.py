class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        nexts= 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nexts += 1
                
            result += nexts
        return result
        
        return ans
        
        


        