class Solution(object):
    def totalFruit(self, fruits):
        ans=0
        l=0
        check={}
        for r in range(len(fruits)):
            if fruits[r] in check:
                check[fruits[r]]+=1
            else:
                check[fruits[r]]=1
            if len(check)>2:
                while len(check)>2 and l<r:
                    if fruits[l] in check:
                        check[fruits[l]]-=1
                        if check[fruits[l]]==0:
                            del check[fruits[l]]
                    l+=1
            ans=max(ans,r-l+1)
        return ans

        