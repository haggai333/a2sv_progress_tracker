class Solution:
    def isSubset(self, a, b):
        joind = {}
        for i in a:
            if i in joind:
                joind[i] += 1
            else:
                joind[i] = 1
        for i in b:
            if i not in joind or joind[i] == 0:  
                return False
            joind[i] -= 1 
        
        return True  
