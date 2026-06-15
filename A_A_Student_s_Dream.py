girl=list(map(int,input().split()))
boy=list(map(int,input().split()))

if abs(boy[0]-girl[1])<abs(boy[1]-girl[0]):
    answer=boy[0]-girl[1]
    state=0
    if boy[0]>=girl[1] and answer<2:
        state+=1
    if boy[0]<girl[1] and answer>=-1:
        state+=1
    if state>0:
        print("YES")
    else:
        print("NO")
    
else:
    answer=boy[1]-girl[0]
    state=0
    if boy[1]>=girl[0] and answer<2:
        state+=1
    if boy[1]<girl[0] and answer>=-1:
        state+=1
    if state>0:
        print("YES")
    else:
        print("NO")
   
   