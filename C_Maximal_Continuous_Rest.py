class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
n=int(input())
a=list(map(int,input().split()))
if n>0:
    head=Node(-1)
    temp=head
    for i in a:
        temp.next=Node(i)
        temp=temp.next
    head=head.next
    if head.next==None:
        if head.val==1:
            print(1)
        else:
            print(0)
    else:
        temp.next=head
        countheads=0
        answer=0
        count=0
        temp=head.next
        while countheads<2:
            if head==temp:
                countheads+=1
            if temp.val!=1:
                answer=max(answer,count)
                count=0
            else:
                count+=1
            temp=temp.next
        answer=max(answer,count)
        print(answer)

