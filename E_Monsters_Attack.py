noofgames=int(input())
for i in range(noofgames):
    line1=list(map(int,input().split()))
    line2=list(map(int,input().split()))
    line3=list(map(int,input().split()))
    noofbullets=line1[1]
    alive=True
    while alive:
        print("new cycle")
        print(line2)
        print(line3)
        pointer=0
        while noofbullets>0 and pointer<line1[0]:
            print("start of loop")
            print(line2)
            print(line3)

            if line2[pointer]==0:
                print("is 0 continue called")
                pointer+=1
                continue
            line2[pointer]-=1
            noofbullets-=1
            pointer+=1
            if noofbullets>0 and pointer==line1[0]-1:
                print("is the last pointer called")
                if line2[pointer]>noofbullets:
                    print("is greater called")
                    line2[pointer]-=noofbullets
                    noofbullets=0
                elif pointer==line1[0]-1:
                    print("is less than called")
                    line2[pointer]=0
                    noofbullets=0
            print("end of the loop")
            print(line2)
            print(line3)        
        for i in range(line1[0]):
            if line2[i]>0 and line3[i]==0:
                alive=False
        won=True
        for i in range(line1[0]):
            if line2[i]!=0:
                won=False
        if won:
            break
        for i in range(line1[0]):
            if line3[i]>0:
                line3[i]-=1
            else:
                line3[i]+=1
        noofbullets=line1[1]
    if alive:
        print("NO")
    else:
        print("YES")

    



    

        
        
        
        

