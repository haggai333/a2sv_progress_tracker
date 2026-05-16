class Node():
    def __init__(self, k):
    
        self.val=k
        self.next=None
        self.prev=None

class MyCircularDeque(object):

    def __init__(self, k):
        self.max=k
        self.size=0
        self.head=None
        self.tail=self.head
        

    def insertFront(self, value):
        current=Node(value)
        if self.size==self.max:
            return False
        if self.head:
            
            current.next=self.head
            self.head.prev=current
            self.head=current
        else:
            self.head=current
            self.tail=current
        self.size+=1
        return True
        
        

    def insertLast(self, value):
        if self.size==self.max:
            return False
        current=Node(value)
        if self.tail:
            
            current.prev=self.tail
            self.tail.next=current
            self.tail=current
        else:
            self.head=current
            self.tail=current
        self.size+=1
        return True

        

    def deleteFront(self):
        if self.head and self.size!=0:
            if self.head.next:
                t=self.head
                self.head=self.head.next
                t.next=None
                self.head.prev=None
            else:
                self.head=None
                self.tail=None
            self.size-=1
            return True
        else:
            return False
        

    def deleteLast(self):
        if self.tail and self.size!=0:
            if self.tail.prev:
                t=self.tail
                self.tail=self.tail.prev
                t.prev=None
                self.tail.next=None
            else:
                self.head=None
                self.tail=None
            self.size-=1
            return True
        else:
            return False
        

    def getFront(self):
        if self.head:
            return self.head.val
        else:
            return -1
        

    def getRear(self):
        if self.tail:
            return self.tail.val
        else:
            return -1
        """
        :rtype: int
        """
        

    def isEmpty(self):
        return self.size==0
        """
        :rtype: bool
        """
        

    def isFull(self):
        return self.size==self.max
        
        


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