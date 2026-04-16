class Solution(object):
    def predictTheWinner(self, nums):
        def checker(l,r):
            if l==r:
                return nums[l]
            return max(nums[l]-checker(l+1,r),nums[r]-checker(l,r-1))
        return checker(0,len(nums)-1)>=0