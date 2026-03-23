n,t=map(int,input().split())
a=list(map(int,input().split()))
answer=0
sum=0
l=0
for r in range(n):
    sum+=a[r]
    while sum>t:
        sum-=a[l]
        l+=1
    answer=max(r-l+1,answer)
    
    
print(answer)


    

