size,winsize=map(int,input().split())
arr=list(map(int,input().split()))
l=0
r=0
arr.sort()
sum=0
length=0

while r<size:
    if sum==winsize:
        length=max(length,r-l+1)
    if sum>=winsize:
        sum-=arr[l]
        l+=1
    if sum<winsize:
        sum+=arr[r]
        r+=1
print(length)


