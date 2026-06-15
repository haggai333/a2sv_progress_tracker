n=int(input())
answer=set()
for i in range(2,n+1):
    check=set()
    p=2
    temp=i
    while p<temp and i>1:
        if i%p==0:
            check.add(p)
            i//=p
        else:
            p+=1
    if len(check)==2:
        answer.add(temp)
print(len(answer))
    