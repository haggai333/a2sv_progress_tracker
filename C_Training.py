size=int(input())
sumi=list(map(int,input().split()))
answer=0
sumi.sort()
day=1
for i in sumi:
    if i<day:
        continue
    day+=1
    answer+=1
print(answer)
