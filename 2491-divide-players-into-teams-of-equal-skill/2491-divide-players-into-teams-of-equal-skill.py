class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l=0
        r=len(skill)-1
        groups=[]
        k=skill[l]+skill[r]
        answer=0
        while(r>l):
            if k!=skill[l]+skill[r]:
                return -1
            answer+=skill[l]*skill[r]
            r-=1
            l+=1
        
        return answer
        

        