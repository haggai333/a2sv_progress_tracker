class Solution:    
    def findUnion(self, a, b):
        uniond=set()
        for i in a:
            uniond.add(i)
        for j in b:
            uniond.add(j)
        
        return list(uniond)
        