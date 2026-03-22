class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        answer= 0
        temp = 0
        l = 0
        counter = set()
        for r in range(len(nums)):
            while nums[r] in counter:
                counter.remove(nums[l])
                temp -= nums[l]
                l += 1
            temp += nums[r]
            counter.add(nums[r])
            answer = max(answer,temp)

        return answer
        