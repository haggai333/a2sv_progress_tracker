t=int(input())
for _ in range(t):
    ist=True
    n,c,d=map(int,input().split())
    a=list(map(int,input().split()))
    print(a)
    og=a[0]
    i=1
    while i<len(a) and ist:
        if i%n==0:
            if a[i]-og==c:
               print(i,"ok")
               og=a[i]
               i+=1
               continue
            else:
               print(i,"not ok")
               ist=False
        print(i)
        i+=1
    print(ist)
