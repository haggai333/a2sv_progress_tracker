t=int(input())
for _ in range(t):
    size=int(input())
    arr=list(map(int,input().split()))
    mid=1
    if len(arr)<3:
        print("NO")
        continue
    found=False
    answer=[0,0,0]
    for l in range(size-2):
        mid=l+1
        r=mid+1
        if arr[l]>arr[mid]:
            continue
        while r<size:
            if arr[mid]>arr[r]:
                answer[0]=l+1
                answer[1]=mid+1
                answer[2]=r+1
                found=True
                
            r+=1
        
        
        
    if found:
        print(*answer)
        print("YES")
    else:
        print("NO")
