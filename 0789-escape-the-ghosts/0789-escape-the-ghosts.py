class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ghostdistance=[]
        mydistance=abs(target[0])+abs(target[1])
        for i in ghosts:
           if abs(i[0]-target[0])+abs(i[1]-target[1])<=mydistance:
            return False
        return True
        