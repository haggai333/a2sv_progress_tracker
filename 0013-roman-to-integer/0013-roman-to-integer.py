class Solution(object):
    def romanToInt(self, s):
        check={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        answer=0
        prev=0
        for i in range(len(s)-1,-1,-1):
            if check[s[i]]>=prev:
                answer+=check[s[i]]
            else:
                answer-=check[s[i]]
            prev=check[s[i]]
        
        return answer

        