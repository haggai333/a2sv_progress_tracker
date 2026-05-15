t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input().strip()
    counts={}
    found=False
    for i in s:
        counts[i]=1+counts.get(i,0)
    if counts.get('B',0)==k:
        print(0)
        continue
    lists=[0]*(n+1)
    for i in range(n-1,-1,-1):
        lists[i]=lists[i+1]+(s[i]=='B')
    for i in range(1,n+1):
        if i+lists[i]==k:
            print(1)
            print(i,'B')
            found=True
            break
        if lists[i]==k:
            print(1)
            print(i,'A')
            found=True
            break
    if not found:
        print(2)
        print(n,'A')
        print(k,'B')
    