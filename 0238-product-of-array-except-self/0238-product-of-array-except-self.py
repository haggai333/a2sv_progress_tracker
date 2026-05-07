class Solution(object):
    def productExceptSelf(self, nums):
        prefix=[]
        current=1
        haszero=nums.count(0)
        if nums.count(0)>1:
            return [0]*len(nums)
        for i in nums:
            if i==0:
                continue
            else:
                current*=i
        for i in nums:
            if haszero!=0 and i==0:
                prefix.append(current)
            elif haszero==0 and i!=0:
                prefix.append(current//i)
            else:
                prefix.append(0)
        return prefix

        