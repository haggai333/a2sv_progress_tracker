class Solution(object):
    def combinationSum(self, candidates, target):
        answer=[]
        path=[]
        exists=set()
        def backtrack(currentsum,j):
            if currentsum==target:
                answer.append(path[:])
                return
            if currentsum>target:
                return
            for p,i in enumerate(candidates):
                    if p<j:
                        continue
                    currentsum+=i
                    path.append(i)
                    backtrack(currentsum,p)
                    currentsum-=i
                    path.pop()
        backtrack(0,0)
        return answer

        