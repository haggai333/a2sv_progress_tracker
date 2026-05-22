class Solution(object):
    def permute(self, nums):
        answer=[]
        path=[]
        self.count=0
        used=set()
        size=math.factorial(len(nums))
        def backtrack(j):
            if self.count==size:
                return
            if j==len(nums):
                answer.append(path[:])
                self.count+=1
                return
            for i in nums:
                if i not in used:
                    used.add(i)
                    path.append(i)
                    backtrack(j+1)
                    used.discard(i)
                    path.pop()
                

            
            
            
            
        backtrack(0)
        return answer
        