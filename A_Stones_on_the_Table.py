size=int(input())
a=input()
answer=0
for i in range(size-1):
    if a[i]==a[i+1]:
        answer+=1
print(answer)
