class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        count=0
        answer1={}
        answer2={}
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count+=1
            if s1[i] in answer1:
                answer1[s1[i]]+=1
            else:
                answer1[s1[i]]=1
            if s2[i] in answer2:
                answer2[s2[i]]+=1
            else:
                answer2[s2[i]]=1
        
        return count<=2 and answer1==answer2
        

        