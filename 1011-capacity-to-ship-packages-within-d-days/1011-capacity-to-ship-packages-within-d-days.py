class Solution(object):
    def shipWithinDays(self, weights, days):
        l=max(weights)
        r=sum(weights)
        while l<r:
            mid=(l+r)//2
            count=0
            cumli=0
            for i in weights:
                if cumli+i>mid:
                    count+=1
                    cumli=i
                else:
                    cumli+=i
                if count+1>days:
                    break
            if count+1>days:
                l=mid+1
            else:
                r=mid
        return l


        