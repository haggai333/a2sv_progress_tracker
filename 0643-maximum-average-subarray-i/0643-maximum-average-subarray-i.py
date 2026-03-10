class Solution(object):
    def findMaxAverage(self, nums, k):
        if k==1:
            return max(nums)
        count=0
        l=0
        r=0
        sum=count
        done=True
        while r<len(nums):
            if r<k and done:
                count+=nums[r]
                if r-l==k-1:
                    done=False
                    sum=count
                r+=1
                continue
            else:
                count+=(nums[r]-nums[l])
                sum=max(sum,count)
                r+=1
                l+=1
        return sum/float(k)