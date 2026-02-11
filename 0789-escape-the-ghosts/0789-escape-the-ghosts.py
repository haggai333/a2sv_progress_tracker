class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ghostdistance=[]
        mydistance=abs(target[0])+abs(target[1])
        print(mydistance)
        for i in ghosts:
            ghostdistance.append([abs(i[0]-target[0])+abs(i[1]-target[1]),abs(i[0]+i[1])])
        print(ghostdistance)
        for i in ghostdistance:
            if i[0]<=mydistance :
                return False
        return True
        