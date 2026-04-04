# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        if not head:
            return None
        lessthan=ListNode(-1)
        greaterthan=ListNode(-1)
        a=lessthan
        b=greaterthan
        

        while head:
            if head.val<x:
                lessthan.next=ListNode(head.val)
                
                lessthan=lessthan.next
            else :
                greaterthan.next=ListNode(head.val)
                
                greaterthan=greaterthan.next

            head=head.next
        a=a.next
        b=b.next
        answer=a
        if not a:
            return b
        while a.next:
            a=a.next
        
        a.next=b
        return answer

        