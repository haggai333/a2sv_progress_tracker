t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    possible= [0] * (k+1)
    for _ in range(k):
        bi,ci=map(int,input().split())
        possible[bi]+=ci
        
    if len(possible)<=n:
        print(sum(possible))
    else:
        answer=0
        possible.sort(reverse=True)
        for i in range(n):
            answer+=possible[i]
        print(answer)