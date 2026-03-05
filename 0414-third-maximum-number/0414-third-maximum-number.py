class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums))<3:
            return max(nums)
        count=0
        nums.sort(reverse=True)
        maxi=nums[0]
        for i in nums:
            if i <maxi:
                maxi=i
                count+=1
            if count==2:
                break
        return maxi
        