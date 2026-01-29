class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashval={}
        for i in range(len(nums)):
            if target-nums[i] in hashval:
                return [i,hashval[target-nums[i]]]
            hashval[nums[i]]=i
        return []