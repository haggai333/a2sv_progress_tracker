class Solution(object):
    def findContentChildren(self, g, s):
        g.sort(reverse=True)
        s.sort(reverse=True)
        answer=0
        while g and s:
            if s[-1]>=g[-1]:
                answer+=1
                g.pop()
                s.pop()
            else:
                s.pop()
        return answer

        