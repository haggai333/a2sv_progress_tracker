class Solution(object):
    def isCovered(self, ranges, left, right):
        l=set()
        for i in ranges:
            for j in range(i[0],i[len(i)-1]+1):
                if j>=left and j<=right:
                    l.add(j)
        
        for i in range(left,right+1):
            if i in l:
                continue
            return False
        return  True


        
        


        