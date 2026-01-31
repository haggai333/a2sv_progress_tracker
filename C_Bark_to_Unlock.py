password=input()
size=int(input())
listval=[]
first=False
second=False
fullstring=""
for i in range(size):
    s=input()
    fullstring+=s
    listval.append(s)
for i in listval:
    if password[0]==i[1]:
        second=True
    if password[1]==i[0]:
        first=True
if first and second or password in fullstring:
    print("YES")
else:
    print("NO")