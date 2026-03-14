class Solution(object):
    def appendCharacters(self, s, t):
        answer=len(t)
        l=0
        r=0
        while l<len(s) and r<len(t):
            if s[l]==t[r]:
                answer-=1
                l+=1
                r+=1
            else:
                l+=1
        return answer
        