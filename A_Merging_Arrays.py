n=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=0
r=0
answer=[]
while l<n[0] or r<n[1]:
    if l<n[0] and r<n[1]:
        if a[l]>b[r]:
            answer.append(b[r])
            r+=1
            continue
        else:
            answer.append(a[l])
            l+=1
            continue

    if r<n[1]:
        answer.append(b[r])
        r+=1

    if l<n[0]:
         answer.append(a[l])
         l+=1
print(*answer)