t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    p={}
    for i in a:
        if i in p:
            p[i]+=1
        else:
            p[i]=1
    m=[]
    for i in p:
        m.append([i,p[i]])
    m.sort()
    for i in m:
        if i[1]==2:
            return i[1]-
    print(m)

    

    