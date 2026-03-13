class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        temp=[]
        for i in intervals:
            temp.append(i[0])
            temp.append(i[1])
        print temp
        answer=[]
        l=0
        for i in range(1,len(temp)-1):
            if i%2==0 and i>0:
                if temp[i]>temp[i-1]  and temp[i]>=temp[i+1]:
                    continue
                else:
                    answer.append([temp[l],temp[i+1]])
                    l=i+2
            
        return answer




        
            
        