n=int(input())
checker={}
for j in range(n):
    m=int(input())
    for i in range(m):
        name,time=list(map(str,input().split()))
        ans=name+time
        if ans in checker:
            checker[ans]+=1
        else:
            checker[ans]=1
broken=False
for i in checker:
    if (checker[i]/n)>=0.8:
        print("YES")
        broken=True
if not broken:
    print("NO")

    

