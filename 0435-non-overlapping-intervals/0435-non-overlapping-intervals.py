class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x:x[0])
        count=0
        end=intervals[0][1]
        for i in intervals:
            if i[0]<end:
                count+=1
                end=min(end,i[1])
            else:
                end=i[1]
        return count-1


        