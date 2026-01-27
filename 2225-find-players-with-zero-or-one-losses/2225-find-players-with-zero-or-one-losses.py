class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        rank={}
        answer=[[],[]]
        for i in matches:
            if i[0] not in rank:
                rank[i[0]]=0
            if i[1] in rank:
                rank[i[1]]-=1
            else:
                rank[i[1]]=-1
        
        for j in rank:
            if rank[j]==0:
                answer[0].append(j)
            if rank[j]==-1:
                answer[1].append(j)
        answer[0].sort()
        answer[1].sort()
            
        return answer
