size ,t=map(int,input().split())
arr=input()
answer=[]
for i in arr:
    answer.append(i)
for _ in range(t):
    i=1
    while i<size:
        if answer[i-1]=='B'and answer[i]=='G':
            answer[i-1],answer[i]=answer[i],answer[i-1]
            i+=2
        else:
            i+=1
print("".join(answer))