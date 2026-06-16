n,k=map(int,input().split())
answer=[]
turn=0
for i in range(n):
    temp=[]
    for j in range(k):
        if i%2==0:
            temp.append("#")
        else:
            if turn==1:
                if j==0:
                    temp.append("#")
                else:
                    temp.append(".")
            else:
                if j==k-1:
                    temp.append("#")
                else:
                    temp.append(".")
    if i%2==1:
        turn=abs(turn-1)
    answer.append("".join(temp))
for i in answer:
    print(i)