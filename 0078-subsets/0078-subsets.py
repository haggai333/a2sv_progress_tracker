class Solution(object):
    def subsets(self, nums):
        answer=[]
        def backtrack(i,nums,t):
            if i==len(nums):
                answer.append(t)
                return
            
            backtrack(i+1,nums,t[:])
            t.append(nums[i])
            
            backtrack(i+1,nums,t[:])
        backtrack(0,nums,[])
        return answer
        
        