t=int(input())
for _ in range(t):
    count={}
    size=int(input())
    s=input()
    if size%2==1:
        print("NO")
    else:
        for i in s:
            count[i]=1+count.get(i,0)
        if count.get("(",0)==count.get(")",0):
            print("YES")
        else:
            print("NO")