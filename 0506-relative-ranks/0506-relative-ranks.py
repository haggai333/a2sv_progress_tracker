class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s=score.copy()
        s.sort(reverse=True)
        a={}
        for i in range(len(s)):
            a[s[i]]=i
        answer=[]
        for i in score:
            if a[i]==0:
                answer.append("Gold Medal")
            elif a[i]==1:
                answer.append("Silver Medal")
            elif a[i]==2:
                answer.append("Bronze Medal")
            else:
                answer.append(str(a[i]+1))
        return answer

        