class Solution(object):
    def judgeSquareSum(self, c):
        r=sqrt(c)
        r=int(r//1)
        
        temp=[]
        for i in range(r+1):
            temp.append(i*i)
        l=0
        
        r=len(temp)-1
        while(r>=l):
            if temp[r]+temp[l]<c:
                l+=1
            elif temp[r]+temp[l]>c:
                r-=1
            else:
                return True
        return False

        