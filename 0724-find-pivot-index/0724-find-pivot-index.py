class Solution(object):
    def pivotIndex(self, nums):
        left=[nums[0]]
        right=[nums[-1]]
        size=len(nums)
        for i in range(1,size):
            left.append(left[-1]+nums[i])
            right.append(right[-1]+nums[size-i-1])
        for i in range(size):
            if left[i] - nums[i] == right[size-i-1] - nums[i]:
                return i
        return -1

        