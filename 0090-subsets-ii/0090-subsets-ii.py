class Solution(object):
    def subsetsWithDup(self, nums):
        answer=[]
        path=[]
        nums.sort()
        def backtrack(count):
            if count>len(nums):
                return
            answer.append(path[:])
            while count<len(nums):
                path.append(nums[count])
                backtrack(count+1)
                path.pop()
                while count<len(nums)-1 and nums[count]==nums[count+1]:
                    count+=1
                count+=1
        backtrack(0)
        return answer