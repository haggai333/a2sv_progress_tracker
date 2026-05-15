t=int(input())
for _ in range(t):
    n=int(input())
    health=list(map(int,input().split()))
    timeleft=list(map(int,input().split()))
    p=[]
    for i in range(n):
        p.append([timeleft[i],health[i]])
    p.sort()
    totaltime=max(timeleft)
    answer=1
    for i in p:
        if i[1]/answer<totaltime:
            totaltime
