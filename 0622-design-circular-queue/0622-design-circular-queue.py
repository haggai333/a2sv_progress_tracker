class Node():
    def __init__(self, k):
    
        self.val=k
        self.next=None
        self.prev=None
    
class MyCircularQueue(object):

    def __init__(self, k):
        self.max=k
        self.size=0
        self.head=None
        self.tail=self.head
    def enQueue(self, value):
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
        

    def deQueue(self):
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
        

    def Front(self):
        if self.head:
            return self.head.val
        else:
            return -1
        

    def Rear(self):
        if self.tail:
            return self.tail.val
        else:
            return -1
        
        

    def isEmpty(self):
        return self.size==0 and not self.head
        

    def isFull(self):
        return self.size==self.max
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()