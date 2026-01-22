class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        a=0
        b=x
         
            
        while(b>0):
            a=(10*a)+(b%10)
            b=b/10
         
        
        return a==x    
            
        