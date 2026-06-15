n ,t=map(int,input().split())
for _ in range(t,0,-1):
    if n%10==0:
        n//=10
    else:
        n-=1
print(n)