class Solution(object):
    def balancedString(self, s):
        count={}
        current=len(s)//4
        answer=float('inf')
        for i in s:
            count[i]=1+count.get(i,0)
        if all(count.get(c,0)<=current for c in "QWER"):
            return 0
        l=0
        r=0
        while r<len(s):
            count[s[r]]-=1
            while l<=r and all(count.get(c, 0)<=current for c in "QWER"):
                answer=min(answer,r-l+1)
                count[s[l]]+=1
                l+=1
            r+=1
        

        return answer
        
        