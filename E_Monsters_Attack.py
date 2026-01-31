noofgames=int(input())
for i in range(noofgames):
    line1=input().split()
    line2=input().split()
    line3=input().split()
    noofbullets=int(line1[1])
    noofmonstors=int(line1[0])
    neworderedlist=[]
    for i in range(int(noofmonstors)):
        neworderedlist.append([int(line3[i]),int(line2[i])])
    neworderedlist.sort()
    
    current=0
    alive=True
    print(neworderedlist)
    while alive and current<noofmonstors:
        print(current)
        print(neworderedlist[current])
        if  neworderedlist[current][0]>0 or neworderedlist[current][0]<0:
            if neworderedlist[current][0]>0:
                if neworderedlist[current][1]>noofbullets:
                    neworderedlist[current][1]-=noofbullets
                    print([neworderedlist[current][1]])
                    print("positive")
                    continue
                else:
                    neworderedlist[current][1]=0
                    print("positive")
            else:
                if (neworderedlist[current][1])>noofbullets:
                    neworderedlist[current][1]+=noofbullets
                    print([neworderedlist[current][1]])
                    print("negative")
                    continue
                else:
                    neworderedlist[current][1]=0
                    print("negative 0")
        print(neworderedlist[current])

        if neworderedlist[current][0]!=0:
            print("NO")
            alive=False
            
        else:
            current+=1
    if alive:
        print("YES")

        
        
        
        

