a=list(map(int,input().split()))
p=list(map(int,input().split()))
a.sort()
j=0
for i in range(a[1]):
    if j<=len(p):
        print(0)
        continue
    k=a[j]
    for i in p:
        if i<k and i>0:
           
            k=i
    
     
    for i in range(len(p)):
        if p[i]>0:
            p[i]-=k
    j+=1
    print(k)