class Solution(object):
    def maxScore(self, cardPoints, k):
        if len(cardPoints)==k:
            return sum(cardPoints)
        sums=sum(cardPoints)
        windowsize=len(cardPoints)-k
        print(windowsize)
        l=0
        tempsum=0
        answer=0
        for r in range(len(cardPoints)):
            tempsum+=cardPoints[r]
            if r-l==windowsize-1:
                
                answer=max(answer,sums-tempsum)
                tempsum-=cardPoints[l]
                l+=1
                print(l,r,tempsum,answer)
        return answer
                


        