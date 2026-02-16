t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    result="YES"
    b=[]
    b=a.copy()
    counts=1
    r=0
    reverss=False
    
    while(counts<(2*(len(a))-1)+1):
        if r==len(a)-1:
            reverss=True
        if reverss:
            for i in a:
                i-=1
            
            r-=1
            if b.count(0)>0:
                result="NO"
                break
            counts+=1
            
        else:
            for i in a:
                i-=1
            
            r+=1
            
            if b.count(0)>0:
                result="NO"
                break
            counts+=1
            r+=1
        
       
        
        

    print(result)