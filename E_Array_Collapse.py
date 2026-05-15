t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    test=input().strip()
    product=1
    zerocount=0
    l=0
    r=len(arr)-1
    for i in arr:
        if i==0:
            zerocount+=1
            continue
        product*=i
    answer=[]
    for i in test:
        if i=="L":
            if zerocount>0:
                answer.append(0)
            else:
                answer.append(int(product%m))
                product/=arr[l]
            if arr[l]==0:
                    zerocount-=1
            l+=1
        else:
            if zerocount>0:
                answer.append(0)
            else:
                answer.append(int(product%m))
                product/=arr[r]
            if arr[r]==0:
                    zerocount-=1
            r-=1
        
    print(*answer)
            
   
        
    