n,d=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
available=n-1
i=0
answer=[]

if n==1:
    if arr[0]>d:
        print(1)
    else:
        print(0)
else:
    while available>0 and i<n:
        
        counts=arr[i]
        while counts<d and available>0:
            counts+=arr[i]
            available-=1
        
        if counts>d:
            
            answer.append(counts)
        i+=1
    
    print(len(answer))

