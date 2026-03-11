class Solution(object):
    def findAnagrams(self, s, p):
        checker=set(p)
        check=set()
        l=0
        r=0
        answer=[]
        while r<len(s):
            check.add(s[r])
            r+=1
            if r-l==len(checker):
                if check==checker:
                    answer.append(l)
                if s[l]==s[r-1]:
                    l+=1
                    continue
                check.discard(s[l])
                l+=1
        return answer



        