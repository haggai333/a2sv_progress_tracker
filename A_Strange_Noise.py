class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
t=int(input())
for _ in range(t):
    size=int(input())
    s=input()
    s=s.lower()
    answer=list("meow")
   
    a=[]
    prev=None
    for i in s:
        if i==prev:
            continue
        prev=i
        a.append(i)
    correct=True
    if len(a)!=4:
        correct=False
    i=0
    while correct and i<4:
        if answer[i]!=a[i]:
            correct=False
        i+=1
    if correct:
        print("YES")
    else:
        print("NO")


        
    

        
