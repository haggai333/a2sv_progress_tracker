class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        nexts=0
        print(nums)
        for i in range(len(nums)-1,1,-1):
            if nums[i]!=nums[i-1]:
                nums[i]=nums[i-1]
                result+=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[i]=nums[i-1]
                result+=1

            
        return result
        
        


        