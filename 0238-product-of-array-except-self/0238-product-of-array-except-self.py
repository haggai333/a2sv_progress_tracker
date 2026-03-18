class Solution(object):
    def productExceptSelf(self, nums):
        left=[]
        left.append(1)
        for i in range(len(nums)-1):
            left.append(nums[i]*left[i])
        
        right=[]
        right.append(1)
        for i in range(len(nums)-1,0,-1):
            right.append(nums[i]*right[len(nums)-i-1])
        right.reverse()
        answer=[]
        for i in range(len(nums)):
            answer.append(left[i]*right[i])
        return answer

       
      
        
        