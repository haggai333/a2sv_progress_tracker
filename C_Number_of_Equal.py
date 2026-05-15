size1,size2=map(int,input().split())
count1={}
count2={}
seen=set()
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
answer=0
for i in arr1:
    count1[i]=1+count1.get(i,0)
for j in arr2:
    count2[j]=1+count2.get(j,0)
for j in arr1:
    if j not in seen:
        temp=(count1.get(j,0)*count2.get(j,0))
        answer+=temp
        seen.add(j)
print(answer)


