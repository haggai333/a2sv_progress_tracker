class Solution(object):
    def checkInclusion(self, s1, s2):
        count={}
        counter={}
        l=0
        for i in s1:
            count[i]=1+count.get(i,0)
        for r,i in enumerate(s2):
            if i in count:
                counter[i]=1+counter.get(i,0)
            if  counter==count:
                return True
            while i in counter and counter[i]>count[i] and l<r:
                if s2[l] in counter:
                    counter[s2[l]]-=1
                l+=1

            if i not in count:
               
                l=r
                counter.clear()
            
        return False
        