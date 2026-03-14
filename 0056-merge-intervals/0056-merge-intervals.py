class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        answer=[]
        l=0
        if len(intervals)<2:
            return intervals
        for i in range(1,len(intervals)):
            if intervals[i][0] > intervals[i-1][1]:
                answer.append([intervals[l][0], intervals[i-1][1]])
                l=i
            else:
                intervals[i][1] = max(intervals[i][1], intervals[i-1][1])

        answer.append([intervals[l][0], intervals[-1][1]])
       
        return answer




        
            
        