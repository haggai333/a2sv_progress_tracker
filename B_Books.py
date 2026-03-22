n,t=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
count=0
sum=0
temp=0
l=0
while l<len(a):
    temp+=a[l]
    if temp<=t and l<n:
        sum=l+1
    l+=1
print(sum)


    

