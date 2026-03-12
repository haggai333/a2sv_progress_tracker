class Solution(object):
    def numberOfSubarrays(self, nums, k):
        answer = 0
        noodds = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                noodds += 1
            while noodds > k:
                if nums[l] % 2 == 1:
                    noodds -= 1
                l += 1
            if noodds == k:
                temp = l
                while temp <= r and nums[temp] % 2 == 0:
                    answer += 1
                    temp += 1
                answer += 1

        return answer