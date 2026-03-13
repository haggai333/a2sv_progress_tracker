class Solution(object):
    def maxVowels(self, s, k):
        a="aeiou"
        l=0
        count=0
        answer=0
        for r in range(len(s)):
            if s[r] in a:
                count+=1
            r+=1
            
            if r-l==k+1:
                if s[l] in a:
                    count-=1
                l+=1
            answer=max(answer,count)
        return answer