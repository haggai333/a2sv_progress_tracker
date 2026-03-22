class Solution(object):
    def judgeSquareSum(self, c):
        r=int(sqrt(c))
        l=0
        while(r>=l):
            if (r*r)+(l*l)<c:
                l+=1
            elif (r*r)+(l*l)>c:
                r-=1
            else:
                return True
        return False

        