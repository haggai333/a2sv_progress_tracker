test=int(input())
for i in range(test):
    n=int(input())
    temp=[]
    for i in range(n):
        a,b=map(int,input().split())
        temp.append((a,b))
    
    temp.sort(key=lambda x:(min(x),max(x)))
    ans=[]
    for i in range(n):
        a,b=temp[i]
        ans.append(a)
        ans.append(b)
    print(*ans)