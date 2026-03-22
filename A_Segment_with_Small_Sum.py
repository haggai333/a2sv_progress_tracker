size,winsize=map(int,input().split())
arr=list(map(int,input().split()))
l=0
r=0
sum=0
length=0

for r in range(size):
    sum+=arr[r]
    while sum>winsize:
        sum-=arr[l]
        l+=1
    length=max(length,r-l+1)

print(length)


