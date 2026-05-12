class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x:x[0])
        count=0
        end=intervals[0][1]
        start=intervals[0][0]
        for i in intervals:
            if i[1]>start and i[1]<end or start>i[0] and start<i[1] or end>i[0] and end<i[1] or i[0]<end and i[0]>start:
                count+=1
                
                if i[1]<end:
                    end=i[1]
                    start=i[0]

            elif start==i[0] and end==i[1]:
                
                count+=1
                if i[1]<end:
                    end=i[1]
                    start=i[0]
            else:
                start=i[0]
                end=i[1]
            
        return count-1

        