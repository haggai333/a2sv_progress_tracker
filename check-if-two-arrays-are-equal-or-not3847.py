class Solution:
    def checkEqual(self, a, b) -> bool:
        checker={}
        for i in a:
            if i in checker:
                checker[i]+=1
            else:
                checker[i]=1
        for i in b:
            if i in checker:
                if checker[i]>0:
                    checker[i]-=1
                    continue
            return False
        return True