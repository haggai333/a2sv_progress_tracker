a,b=map(int,input().split())
answer=[]

if a/2 <b:
    print(int(b-(a/2))*2)
else:
    print(2*b-1)