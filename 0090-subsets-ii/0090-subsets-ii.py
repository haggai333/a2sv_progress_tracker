class Solution(object):
    def subsetsWithDup(self, nums):
        answer=[]
        path=[]
        used=set()
        nums.sort()
        def backtracking(counts):
            if counts>len(nums):
                return
            answer.append(path[:])
            
            
            while counts<len(nums):
                path.append(nums[counts])
                backtracking(counts+1)
                path.pop()
                while counts<len(nums)-1 and nums[counts]==nums[counts+1]:
                    counts+=1
                counts+=1
                
        backtracking(0)
        return answer
                
        