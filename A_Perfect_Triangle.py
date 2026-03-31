t = int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    answer=float('inf')
    for i in range(n - 2):
        temp=a[i+2]-a[i]
        answer=min(answer,temp)
    print(answer)