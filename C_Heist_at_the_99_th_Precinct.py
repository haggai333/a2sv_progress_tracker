t=int(input())
for i in range(t):
    k=int(input())
    a=list(map(int,input().split()))
    
    mx=0
    a.sort()
    count=0
    
    for i in range(0,len(a)):
        p=len(a)-i-1
        if a[p]>=mx:
            mx=a[p]
            a[p]=0
            
        else:
            break
        count+=1
    if count%2==1 and count!=0:
        print("YES")
    else:
        print("NO")
    
    
        