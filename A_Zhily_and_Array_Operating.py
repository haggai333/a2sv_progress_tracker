t=int(input())
for _ in range(t):
    size=int(input())
    arr=list(map(int,input().split()))
    answer=0
    for i in range(size-1,-1,-1):
       
        if i<size-1 and arr[i+1]>0:
            arr[i]+=arr[i+1]
        if arr[i]>0:
            answer+=1
    print(answer)
