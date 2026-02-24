n=int(input())
p=n
for i in range(p):
    l,r=list(map(int,input().split()))
    thelist=list(map(int,input().split()))
    answer=""
    for j in range(r):
        n=list(map(str,input().split()))
        for k in range(len(thelist)):
            if thelist[k]>=int(n[1])and thelist[k]<=int(n[2]):
                if n[0]=="+":
                    thelist[k]+=1
                else:
                    thelist[k]-=1
        answer+=str(max(thelist))+" "
    print(answer)
        



