class Solution(object):
    def findMaxAverage(self, nums, k):
        count=0
        l=0
        r=0
        sum=0
        while r<len(nums):
                count+=nums[r]
                sum=max(sum,count)
                r+=1
                if r-l==k:
                    count-=nums[l]
                    l+=1
        return sum/float(k)