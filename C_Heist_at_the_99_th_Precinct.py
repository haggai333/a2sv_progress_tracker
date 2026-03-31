t = int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    freq=[0]*(n + 1)
    for x in a:
        freq[x]+= 1
    if any(i%2==1 for i in freq):
        print("YES")
    else:
        print("NO")