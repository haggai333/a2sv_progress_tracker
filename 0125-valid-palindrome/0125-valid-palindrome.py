class Solution(object):
    def isPalindrome(self, s):
        k=""
        for i in s:
            if i>='a'and i<='z'or i>="A"and i<="Z" or i>="0"and i<="9":
                k+=i.lower()
        l=0
        r=len(k)-1
        while r>l:
            if k[l]!=k[r]:
                return False
            l+=1
            r-=1
        return True

        