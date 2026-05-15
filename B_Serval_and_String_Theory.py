t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input().strip()
    reverse=s[::-1]
    if s<reverse:
        print("YES")
    elif len(set(s))==1 or k==0:
        print("NO")
    else:
        print("YES")
        