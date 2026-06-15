answer=[0,0]
for i in range(1,7):
    for j in range(1,7):
        if i+j==11:
            answer[0]+=1
        if i+j==12:
            answer[1]+=1
print(answer[0],answer[1])
