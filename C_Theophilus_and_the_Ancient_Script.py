t=int(input())
for i in range(t):
    size=int(input())
    arr=list(input())
    l=0
    if len(arr)>1:
        r=1
    else:
        print(0)
        continue
    swaps=0
    indexes=set()
    while r<=len(arr)-1:
        if arr[l]=="A" and arr[r]=="B" and l not in indexes:
            swaps+=1
            arr[l],arr[r]=arr[r],arr[l]
            indexes.add(l)
            if  l>0 and arr[l-1]=="A" and l-1 not in indexes:
                l-=1
                r-=1
                continue
            l+=1
            r+=1
        else:
            l+=1
            r+=1
        
    print(swaps)


    