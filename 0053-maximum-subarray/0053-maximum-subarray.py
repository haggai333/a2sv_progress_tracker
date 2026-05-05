class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer=float('-inf')
        l=0
        sum=0
        for r in range(len(nums)):
            sum+=nums[r]
            if sum>answer:
                answer=sum
            if sum<0:
                l=r+1
                sum=0
        return answer


        