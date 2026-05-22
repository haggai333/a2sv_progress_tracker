class Solution(object):
    def permute(self, nums):
        answer=[]
        path=[]
        used=set()
        def backtrack():
            if len(path)==len(nums):
                answer.append(path[:])
                return
            for i in nums:
                if i not in used:
                    used.add(i)
                    path.append(i)
                    backtrack()
                    used.discard(i)
                    path.pop()
                

        backtrack()
        return answer
        