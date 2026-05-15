n,m=map(int,input().split())
put=0
i=1
ate=0
for _ in range(n):
    if put==0:
        put+=i
        i+=1
        continue
    if put>m:
        ate+=1
        put-=1
    if put<m:
        put+=i
        i+=1
print(ate)
