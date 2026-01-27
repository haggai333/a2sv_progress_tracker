class Solution(object):
    def isCovered(self, ranges, left, right):
        l=set()
        for i in ranges:
            for j in i:
                if j>left or j<right:
                    l.add(j)
        
        for i in range(left,right+1):
            if i in l:
                continue
            return False
        return  True


        
        


        