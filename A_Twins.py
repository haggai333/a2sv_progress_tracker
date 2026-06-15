size=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
sumi=sum(arr)
answer=0
current=0
for  i in arr:
    current+=i
    answer+=1
    sumi-=i
    if current>sumi:
        break
print(answer)