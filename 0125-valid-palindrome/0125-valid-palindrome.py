class Solution(object):
    def isPalindrome(self, s):
        l=0
        r=len(s)-1
        while r>l:
            if (s[l].isalpha() or (s[l]>='0' and s[l]<='9')) and (s[r].isalpha() or (s[r]>='0' and s[r]<='9')):
                if s[l].lower()!=s[r].lower():
                    return False
                l+=1
                r-=1
                continue
            if not (s[l].isalpha() or (s[l]>="0" and s[l]<="9")) :
                l+=1
            else:
                r-=1
        return True

        