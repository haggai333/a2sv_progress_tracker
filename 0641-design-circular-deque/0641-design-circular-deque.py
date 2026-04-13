class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyCircularDeque(object):
    def __init__(self,k):
        self.size=0
        self.head=None
        self.tail=None
        self.k=k

    def insertFront(self,value):
        if self.size==self.k:
            return False
        node=Node(value)
        if not self.head:
            self.head = self.tail=node
        else:
            node.next=self.head
            self.head=node
        self.size+=1
        return True

    def insertLast(self,value):
        if self.size==self.k:
            return False
        node=Node(value)
        if not self.head:
            self.head=self.tail = node
        else:
            self.tail.next=node
            self.tail=node
        self.size+=1
        return True

    def deleteFront(self):
        if not self.head:
            return False
        self.head=self.head.next
        if not self.head:
            self.tail=None
        self.size-=1
        return True

    def deleteLast(self):
        if not self.head:
            return False
        if self.size==1:
            self.head=self.tail=None
        else:
            temp=self.head
            while temp.next!=self.tail:
                temp=temp.next
            temp.next=None
            self.tail=temp
        self.size-=1
        return True

    def getFront(self):
        return self.head.val if self.head else -1
    def getRear(self):
        return self.tail.val if self.tail else -1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()