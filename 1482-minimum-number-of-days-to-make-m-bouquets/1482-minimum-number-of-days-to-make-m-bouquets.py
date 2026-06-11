class Solution(object):
    def minDays(self, bloomDay, m, k):
        if k*m>len(bloomDay):
            return -1
        r=max(bloomDay)
        l=min(bloomDay)
        while l<r:
            mid=(l+r)//2
            counts=0
            a=0
            for i in bloomDay:
                if i>mid:
                    a=0
                    continue
                a+=1
                if a==k:
                    counts+=1
                    a=0
                
            if counts<m:
                l=mid+1
            else:
                r=mid
        return l
            

        