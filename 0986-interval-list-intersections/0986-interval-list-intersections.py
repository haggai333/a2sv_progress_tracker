class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        l=0
        r=0
        answer=[]
        while r<len(firstList) and l<len(secondList):
            b=min(firstList[r][1],secondList[l][1])
            a=max(firstList[r][0],secondList[l][0])
            if b>=a:
                answer.append([a,b])
            if firstList[r][1]<secondList[l][1]:
                r+=1
            else:
                l+=1
            
        return answer



        