t=int(input())
for _ in range(t):
    s=list(input())
    counts={}
    for i in s:
        counts[i]=1+counts.get(i,0)
    answer=-1
    for i in range(len(s)):
        if counts[s[i]]>1:
            answer=i
            counts[s[i]]-=1
        else:
            break
    if answer==-1:
        print("".join(s))
    else:
        print("".join(s[answer+1:]))
