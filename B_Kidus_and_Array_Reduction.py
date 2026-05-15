t=int(input())
for _ in range(t):
    size=int(input())
    arr=list(map(int,input().split()))
    answer=[]
    for i in arr:
        if not answer:
            answer.append(i)
            continue
        if i>=answer[-1]:
            answer.append(i)
    print(len(answer))
        
        
        
        