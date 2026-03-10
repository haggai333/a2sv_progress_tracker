class Solution(object):
    def findMaxAverage(self, nums, k):
        count=0
        l=0
        r=0
        size=len(nums)
        if k==1:
            return max(nums)
        r=k-1
        for i in range(0,k):
            count+=nums[i]
        r+=1
        sum=count
        while r<size:
            count+=(nums[r]-nums[l])
            sum=max(sum,count)
            r+=1
            l+=1
        return sum/float(k)