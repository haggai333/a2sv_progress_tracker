t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    for i in range(q):
        p=int(input())
        sumi=0
        broken=False
        for i in range(len(arr)):
            sumi+=arr[i]
            if sumi>=p:
                print(i+1)
                broken=True
                break
        if not broken:
            print(-1)


    