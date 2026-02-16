t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    arr=[]
    for i in range(n):
        arr.append(0)
    count=0
    maxi=max(a)
    mini=min(a)
    while  arr!=a:
        for i in arr:
            print("before")
            print(arr)
            if maxi-mini in a:
                if i==(maxi-mini):
                    i=0
                    continue
            i+=(maxi-mini)
            print(i)
        mini=min(a)
        print(arr)
        count+=1
        if count>40:
            break
    





        count+=1

    

    
     
    



