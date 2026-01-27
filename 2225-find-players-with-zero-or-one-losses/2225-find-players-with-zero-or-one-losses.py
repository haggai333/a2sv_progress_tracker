class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        rank={}
        answer=[]
        track=0
        for i in matches:
            if i[0] not in rank:
                rank[i[0]]=0
            if i[1] in rank:
                rank[i[1]]-=1
            else:
                rank[i[1]]=-1
        for i in range(2):
            temp=[]
            for j in rank:
                if i==0 and rank[j]==0:
                    temp.append(j)
                if rank[j]==-1 and i==1:
                    temp.append(j)
            answer.append(temp)
        answer[0].sort()
        answer[1].sort()
        return answer
