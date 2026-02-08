nooftestcase=int(input())
for i in range(nooftestcase):
    noofpeople=int(input())
    if noofpeople<3:
        print(noofpeople)
        continue
    if noofpeople<6:
        print(noofpeople%2)
        continue
    groups=[]
    print(noofpeople)
    while noofpeople>0:
        
        if noofpeople>=3:
            groups.append(3)
            noofpeople-=3
            continue
        if noofpeople>=2:
            groups.append(2)
            noofpeople-=2
        else:
            groups.append(noofpeople)
            noofpeople=0
    print(groups)
    print(29//3)
    if 2 not in groups:
        if len(groups)%2==0:
            print(0)
            continue
        else:
            print(3)
            continue
    if len(groups)%2==0:
        print(1)
    else:
        print(2)
        
  
        
    
        
        
    


   