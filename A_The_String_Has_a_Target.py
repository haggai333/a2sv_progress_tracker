t=int(input())
for _ in range(t):
    size=int(input())
    s=input()
    mini=min(s)
    i=-1
    for j in range(size):
        if s[j]==mini:
            i=j
    result=s[i]+s[:i]+s[i+1:]
    print(result)
        



    

