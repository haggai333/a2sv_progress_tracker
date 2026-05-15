class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        start=intervals[0][0]
        end=intervals[0][1]
        answer=[]
        
        for i in intervals:
            if i[0]<=end and end>i[1]:
                continue
            elif i[0]<=end and end<=i[1]:
                end=i[1]
            else:
                answer.append([start,end])
                start=i[0]
                end=i[1]
        if not answer or start!=answer[-1][0] or end!=answer[-1][1]:
            answer.append([start,end])
        return answer


            