class Solution(object):
    def shiftingLetters(self, s, shifts):
        l=list(s)
        checker=list("abcdefghijklmnopqrstuvwxyz")
        n=len(s)
        sumi=[0]*(n + 1)  
        for start, end, direction in shifts:
            if direction==1:
                sumi[start]+=1
                sumi[end+1]-=1
            else: 
                sumi[start]-=1
                sumi[end+1]+=1
        for i in range(1,n):
            sumi[i]+=sumi[i-1]
        answer = ""
        for i in range(n):
            total=(ord(l[i])-ord('a')+sumi[i])%26
            answer+=checker[total]
        return answer