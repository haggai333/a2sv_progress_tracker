class Solution(object):
    def isPalindrome(self, s):
        k=""
        for i in s:
            if i.isalpha() or i.isdigit():
                k+=i.lower()
        l=0
        r=len(k)-1
        while r>l:
            if k[l]!=k[r]:
                return False
            l+=1
            r-=1
        return True

        