a,b,c=map(int,input().split())
needs=int(a*((c+1)*c/2))
if needs-b>0:
    print(needs-b)
else:
     print(0)
