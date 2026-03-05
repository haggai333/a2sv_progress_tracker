class Solution:
    def frequencySort(self, s: str) -> str:
        a={}
        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        j=[]
        for k in a:
            j.append([a[k],k])
        j.sort( key=lambda x:(-x[0], x[1]))
        a=""
        for i in j:
            for k in range(i[0]):
                a+=i[1]
        return a
        
        
        
        
        