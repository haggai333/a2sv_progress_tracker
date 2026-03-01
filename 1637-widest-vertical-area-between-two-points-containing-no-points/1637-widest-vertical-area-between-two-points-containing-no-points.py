class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l=[]
        maxi=0
        for i in points:
            maxi=max(maxi,i[0])
            l.append(i[0])
        points={}
        for i in l:
            if i in points:
                points[i]+=1
            else:
                points[i]=1
        l=[]
        for i in range(maxi+1):
            if i in points:
                for j in range(points[i]):
                    l.append(i)
        answer=0
        print(l)
        for i in range(0,len(l)-1):
            if answer<(l[i+1]-l[i]):
                answer=l[i+1]-l[i]
            
            
        return answer
            
            
        
        