class Solution(object):
    def removeStars(self, s):
        count=0
        temp=[]
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
            temp.append(s[i])
            i-=1
        l=0
        r=len(temp)-1
        while r>l:
            temp[r],temp[l]=temp[l],temp[r]
            r-=1
            l+=1
        
        return "".join(temp)

        