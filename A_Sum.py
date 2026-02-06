length=int(input())
for i in range(length):
    values=list(map(int,input().split()))
    
    maxi=max(values)
    mini=min(values)
    if maxi-mini in values:
        print("YES")
    else:
        print("NO")