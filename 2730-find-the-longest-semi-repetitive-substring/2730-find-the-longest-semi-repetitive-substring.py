class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        if len(s)<3:
            return len(s)
        pair=0
        size=0
        l=0
        r=0
        for r in range(1,len(s)):
            if s[r-1]==s[r]:
                pair+=1
            if pair>=2:
                c=l+1 
                while pair>=2 and l<r:
                    if s[l]==s[c]:
                        pair-=1
                    l+=1
                    c+=1
            size=max(size,r-l+1)
        return size
        
        