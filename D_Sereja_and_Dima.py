nocard=int(input())
cardlist=list(map(int,input().split()))
firstplayer=0
secondplayer=0
turn=1
start=0
end=nocard-1
for i in range(nocard):
    if turn==1:
        if cardlist[start]>cardlist[end]:
            firstplayer+=cardlist[start]
            start+=1
            turn=0
            continue
        else:
            firstplayer+=cardlist[end]
            end-=1
            turn=0
            continue
    else: 
        if cardlist[start]>cardlist[end]:
            secondplayer+=cardlist[start]
            start+=1
            turn=1
            continue
        else:
            secondplayer+=cardlist[end]
            end-=1
            turn=1
            continue   

print(str(firstplayer)+" "+str(secondplayer))


    
