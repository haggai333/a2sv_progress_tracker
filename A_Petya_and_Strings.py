a=input().lower()
b=input().lower()
answer=0
for i in range(len(b)):
    if ord(a[i])>ord(b[i]):
        answer=1
        break
    if ord(a[i])<ord(b[i]):
        answer=-1
        break
print(answer)