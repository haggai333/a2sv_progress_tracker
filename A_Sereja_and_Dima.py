size=int(input())
arr=list(map(int,input().split()))
sereja=0
dima=0
r=size-1
l=0
turn=0
while r>=l:
    if arr[r]>arr[l]:
        if turn==0:
            sereja+=arr[r]
            r-=1
            turn=1
        else:
            dima+=arr[r]
            r-=1
            turn=0
    else:
        if turn==0:
            sereja+=arr[l]
            l+=1
            turn=1
        else:
            dima+=arr[l]
            l+=1
            turn=0
print(*[sereja,dima])


