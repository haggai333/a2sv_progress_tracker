t=int(input())
for _ in range(t):
    size=int(input())
    a=list(map(int,input().split()))
    b=[]
    for i in a:
        b.append(abs(i))
    b.sort()
    if len(a)==0:
        print("YES")
    else:
        position=b.index(abs(a[0]))
        median=size//2
        if position<=median:
            print("YES")
        else:
            print("NO")
