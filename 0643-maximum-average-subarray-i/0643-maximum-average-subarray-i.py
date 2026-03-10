class Solution(object):
    def findMaxAverage(self, nums, k):
        if k==1:
            return max(nums)
        count=0
        l=0
        r=0
        sum=0
        while r<len(nums):
                count+=nums[r]
                r+=1
                if r-l==k:
                    sum=max(sum,count)
                    count-=nums[l]
                    l+=1
                print(l,r)
                print(count/k)
        return sum/float(k)