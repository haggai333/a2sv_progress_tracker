class Solution(object):
    def combinationSum2(self, candidates, target):
        path=[]
        answer=[]
        candidates.sort()
        def backtrack(currentsum,j):
            if currentsum==target:
                answer.append(path[:])
                return
            if currentsum>target:
                return
            while j<len(candidates):
                if currentsum+candidates[j]<=target:
                    path.append(candidates[j])
                    backtrack(currentsum+candidates[j],j+1)
                    path.pop()
                while j<len(candidates)-1 and candidates[j]==candidates[j+1]:
                    j+=1
                j+=1
        backtrack(0,0)
        return answer


