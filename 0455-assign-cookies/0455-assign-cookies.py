class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        l=0
        r=0
        count=0
        while l<len(g) and r<len(s):
            if s[r]>=g[l]:
                count+=1
                r+=1
                l+=1
            else:
                l+=1
        return count
                