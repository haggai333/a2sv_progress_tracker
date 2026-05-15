n,s=map(int,input().split())
arr=list(map(int,input().split()))
l=0
sumi=0
answer=float("inf")
called=False
for r in range(n):
    sumi+=arr[r]
    while sumi>=s:
        answer=min(answer,r-l+1)
        sumi-=arr[l]
        l+=1
        called=True
if called:
    print(answer)
else:
    print(-1)

    
