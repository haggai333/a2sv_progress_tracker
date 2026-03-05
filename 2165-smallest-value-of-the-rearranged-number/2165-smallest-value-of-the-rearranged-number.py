class Solution:
    def smallestNumber(self, num: int) -> int:
        a=str(num)
        l=list(a.strip())
        
        if num>0:
            l.sort()
        else:
            l.sort(reverse=True)
        if '-' in l:
            l.remove('-')  
        
        if num>0 and '0' in l:
            for i in range(len(l)):
                if int(l[i])>0:
                    l[0]=l[i]
                    l[i]='0'
                    break   
        
        a="".join(l)   
        if num>0:
            return int(a)
        else:
            return -1*int(a)
            
        