class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l=0
        r=len(skill)-1
        groups=[]
        k=skill[l]+skill[r]
        while(r>l):
            if k!=skill[l]+skill[r]:
                return -1
            temp=[]
            temp.append(skill[l])
            temp.append(skill[r])
            groups.append(temp)
            r-=1
            l+=1
        answer=0
        
        for i in groups:
            product=i[0]*i[1]
            answer+=product
            
        return answer
        

        