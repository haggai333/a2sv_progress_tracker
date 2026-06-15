s,n=map(int,input().split())
dragons=[]
for _ in range(n):
    dragons.append(list(map(int,input().split())))
dragons.sort(key=lambda x:x[0])
answer="YES"
for i in dragons:
    if s<=i[0]:
        answer="NO"
        break
    s+=i[1]
print(answer)
