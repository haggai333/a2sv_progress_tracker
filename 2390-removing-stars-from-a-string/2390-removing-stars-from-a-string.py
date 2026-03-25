class Solution(object):
    def removeStars(self, s):
        count=0
        temp=""
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
            temp+=s[i]
            i-=1
        r=len(temp)-1
        answer=""
        while r>-1:
            answer+=temp[r]
            r-=1
        return answer

        