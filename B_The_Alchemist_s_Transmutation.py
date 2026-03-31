t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    o=int(input())
    if min(a)<=o and max(a)>=o:
        print("YES")
    else:
        print("NO")
