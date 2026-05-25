class Solution(object):
    def letterCombinations(self, digits):
        checker=[[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        path=[]
        answer=[]
        def backtrack(count):
            if count==len(digits):
                answer.append("".join(path[:]))
                return
            i=0
            while i<len(checker[int(digits[count])]):
                path.append(checker[int(digits[count])][i])
                backtrack(count+1)
                path.pop()
                i+=1
        backtrack(0)
        return answer
            
        