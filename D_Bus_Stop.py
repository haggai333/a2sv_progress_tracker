n,m=map(int,input().split())
people=list(map(int,input().split()))
nobuses=0
i=0
sum=0
while i<len(people):
    while sum<m and i<len(people):
        if sum+people[i]>m:
            break
        sum+=people[i]
        i+=1
    nobuses+=1
    sum=0
print(nobuses)


