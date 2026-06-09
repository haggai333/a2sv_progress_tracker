class Solution(object):
    def minEatingSpeed(self, piles, h):
        r=max(piles)
        l=1
        while l<r:
            mid=(l+r)//2
            count=0
            for i in piles:
                count+=((i+mid-1)//mid)
            if count>h:
                l=mid+1
            else:
                r=mid
        return l


