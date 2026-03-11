class Solution(object):
    def findAnagrams(self, s, p):
        checker={}
        check={}
        for i in p:
            if i in checker:
                checker[i]+=1
            else:
                checker[i]=1
        l=0
        r=0
        answer=[]
        while r<len(s):
            if s[r] in check:
                check[s[r]]+=1
            else:
                check[s[r]]=1
            r+=1

            if r-l==len(p):
                if check==checker:
                    answer.append(l)
                if s[l] in check:
                    if check[s[l]]>1:
                        check[s[l]]-=1
                    else:
                        del check[s[l]]
                l+=1
            
        return answer



        