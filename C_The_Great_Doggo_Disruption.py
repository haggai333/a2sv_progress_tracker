size=int(input())
s=input()
if size<=1 or len(set(s))==1:
    print("Yes")
else:
    counter={}
    for i in s:
        if i in counter:
            counter[i]+=1
        else:
            counter[i]=1
    greater=0
    lesser=0
    n=[]
    for i in s:
        n.append(counter[i])
    printed=False

    for i in range(1,len(n)):
        if n[i]<n[i-1] and n[i-1]>=2:
            print("Yes")
            printed=True
            break
    if not printed:
        print("No")
        
