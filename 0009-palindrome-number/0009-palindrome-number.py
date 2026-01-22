class Solution(object):
    def isPalindrome(self, x):
        a=0
        b=x
          
            
        while(b>1):
            a=(10*a)+(b/10)
            b=b/10
         
        print(a) 
        return a==x    
            
        