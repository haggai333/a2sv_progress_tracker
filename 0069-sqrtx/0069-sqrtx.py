class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        mid=r+l
        while abs(mid*mid-x)>0.1:
            mid=(r+l)/2
            if mid*mid>x:
                r=mid -1
            elif mid*mid<x:
                l=mid +1
            else:
                return int(mid)
        if round(mid)*round(mid)==x:
            return round(mid)
        else:
            return int(mid)
