size,s=map(int,input().split())
arr=list(map(int,input().split()))
answer=0
l=0
sumi=0
for r in range(size):
    sumi+=arr[r]
    while sumi>s:
        sumi-=arr[l]
        l+=1
    answer+=r-l+1
print(answer)
