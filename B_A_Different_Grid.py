t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    matrix=[]
    if n*m<=1:
        o=list(map(int,input().split()))
        print(-1)
    else:
        unique=0
        p=[]
        cant=False
        for i in range(n):
            o=list(map(int,input().split()))
            o.sort(key=lambda x:x%2==0,reverse=True)
            matrix.append(o)
            for j in o:
                p.append(j)
        k=matrix.copy()
        k.sort(key=lambda x:set(x))
        if k==matrix:
            print(-1)
        else:
            for i in matrix:
                print(*i)

        