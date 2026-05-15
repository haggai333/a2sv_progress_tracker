# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head.next:
            return head
        def reverselist(heads):
            temp=heads
            prev=None
            while temp:
                nexts=temp.next
                temp.next=prev
                prev=temp
                temp=nexts
            return prev
        fast=head
        slow=head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=None
        slow=reverselist(slow)
        temp=head
        prev=None
        while temp or slow:
            if temp and slow:
                next1=temp.next
                next2=slow.next
                temp.next=slow
                temp.next.next=next1
                slow=next2
                prev=temp
                temp=next1
            if not temp:
                while prev.next:
                    prev=prev.next
                prev.next=slow
                break
                
      
        
        return head
        