# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if left==right:
            return head
        def reverselist(head):
            temp=head
            prev=None
            while temp:
                next=temp.next
                temp.next=prev
                prev=temp
                temp=next
            return prev
        size=0
        temp=head
        while temp:
            temp=temp.next
            size+=1
        
        if left==1 and right==size:
            return reverselist(head)
        temp=ListNode(0)
        temp.next=head
        prev=temp
        for i in range(left-1):
            prev=prev.next
        start=prev.next
        end=start
        for i in range(right-left):
            end=end.next
        after=end.next
        end.next=None
        middlepart=reverselist(start)
        prev.next=middlepart
        start.next=after
        return temp.next

        
        
        
        
        