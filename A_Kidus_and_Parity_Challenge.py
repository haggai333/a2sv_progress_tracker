t=int(input())
for _ in range(t):
    size=int(input())
    arr=list(map(int,input().split()))
    answer=[]
    for i in range(1,len(arr)):
            if not answer and (arr[i-1]+arr[i])%2==0:
                answer.append(arr[i-1]) 
                answer.append(arr[i])
                continue
            if (answer[-1]+arr[i])%2==0:
                answer.append(arr[i])
    
    print(size-len(answer))