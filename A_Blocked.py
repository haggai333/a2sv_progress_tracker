t=int(input())
for _ in range(t):
    size=int(input())
    arr=list(map(int,input().split()))
    check=set(arr)
    if len(check)!=len(arr):
        print(-1)
    else:
        arr.sort(reverse=True)
        print(*arr)