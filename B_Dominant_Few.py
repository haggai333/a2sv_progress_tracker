#Skill(Elite)>Skill(Crowd)and Count(Elite)<Count(Crowd)
t=int(input())
for i in range(t):
    size=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    crowdno=0
    crowdpower=0
    elitepower=0
    eliteno=0
    won=False
    r=len(arr)-1
    l=0
    print(arr)
    print("crowd then elite")
    while r>=l:
        if elitepower>crowdpower:
            crowdpower+=arr[l]
            print("added to crowd",arr[l])
            crowdno+=1
            l+=1
        if crowdpower>=elitepower:
            elitepower+=arr[r]
            print("added to elitepower",arr[r])
            eliteno+=1
            r-=1
        print("no of players",crowdno,eliteno)
        print("sum of both",crowdpower,elitepower)
        if elitepower>crowdpower and crowdno>eliteno:
            print("YES")
            won=True
            break
    
    if not won:
        print("NO")
    
    
