class Solution(object):
    def productExceptSelf(self, nums):
        size=len(nums)
        answer=[1]*size
        for i in range(1,size):
            answer[i]=answer[i-1]*nums[i-1]
        suffix=1
        for i in range(size-2,-1,-1):
            suffix*=nums[i+1]
            answer[i]*=suffix
        return answer

            

        