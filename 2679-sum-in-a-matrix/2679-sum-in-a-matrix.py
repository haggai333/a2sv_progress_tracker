class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        total=0
        while len(nums[0])>0:
            maxi=0
            for i in range(len(nums)):
                a=max(nums[i])
                maxi=max(a,maxi)
                nums[i].remove(a)
            total+=maxi
        return total

            
            
            

        