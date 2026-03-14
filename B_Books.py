n,t=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
count=0
l=0
print(a)
while l<len(a) and count<t:
    if a[l]<t:
        count+=1
        t-=a[l]
    l+=1
print(count)

    

