t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=sum(a)
    count=0
    if b%n!=0:
        print(-1)
        continue
    for i in a:
        if i>(b/n):
            count+=1
    print(count)
    