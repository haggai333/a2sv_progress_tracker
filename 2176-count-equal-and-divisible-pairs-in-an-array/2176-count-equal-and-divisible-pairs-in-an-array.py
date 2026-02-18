class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        if len(nums)==len(set(nums)):
            return 0
        size=len(nums)
        for i in range(size - 1):
            for j in range(i + 1, size):
                if nums[i] == nums[j] and (i*j) % k == 0:
                    count += 1
        return count

        


        