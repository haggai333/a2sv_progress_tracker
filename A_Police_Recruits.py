size=int(input())
arr=list(map(int,input().split()))
positive=0
answer=0
for i in arr:
    if positive<0 and i>=0:
        positive=0
    positive+=i
    if positive<0 and i<0:
        answer+=1
print(answer)    
