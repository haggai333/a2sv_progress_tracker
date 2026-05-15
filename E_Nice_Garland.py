size=int(input())
a=list(input())
p=["RGB","RBG","BGR","BRG","GRB","GBR"]
answer=size
answerlist=[]
for i in p:
    k=[]
    count=0
    for j in range(size):
        if a[j]==i[j%3]:
            k.append(a[j])
            continue
        count+=1
        k.append(i[j%3])
    if count<answer:
        answerlist=k
        answer=count
print(answer)
print("".join(answerlist))







        


    

