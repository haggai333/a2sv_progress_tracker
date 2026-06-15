import collections
a=input()
p={}
answer=[]
for i in a:
    p[i]=1+p.get(i,0)
for j in range(1,4):
    counts=0
    if str(j) not in p:
        continue
    if len(answer)<1:
        answer.append(str(j))
        counts+=1
    while counts<p[str(j)]:
        answer.append("+")
        answer.append(str(j))
        counts+=1
print("".join(answer))