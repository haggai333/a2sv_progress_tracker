class Solution(object):
    def removeStars(self, s):
        count=0
        answer=""
        i=len(s)-1
        while i>-1:
            if s[i]=="*":
                count+=1
                i-=1
                continue
            if count>0:
                count-=1
                i-=1
                continue
            answer+=s[i]
            i-=1
        r=len(answer)-1
        temp=""
        while r>-1:
            temp+=answer[r]
            r-=1
        return temp

        