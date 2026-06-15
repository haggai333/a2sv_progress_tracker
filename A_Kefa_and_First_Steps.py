size=int(input())
arr=list(map(int,input().split()))
answer=1
count=1
for r in range(0,len(arr)-1):
    if arr[r+1]>=arr[r]:
        count+=1
    else:
        answer=max(answer,count)
        count=1
print(max(answer,count))

