n=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=0
result=[]
for i in b:
    while l<n[0] and a[l]<i:
        l+=1
    result.append(l)
print(*result)
    