class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        while r>l:
            mid=int(l+(r-l)/2)
            if isBadVersion(mid):
                r=mid
            else:
                l=mid+1
        while r>1 and isBadVersion(r-1):
           r-=1
        return r

        