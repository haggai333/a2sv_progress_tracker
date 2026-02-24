t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    size=len(a)
    result="YES"
    for i in a:
        if i<=2*(size-1):
            result="NO"
            break
        size-=1
    
    print(result)