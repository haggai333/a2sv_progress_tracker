# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if not head.next:
            return True
        def reverselist(heads):
            dummy=heads
            prev=None
            while dummy:
                nexts=dummy.next
                dummy.next=prev
                prev=dummy
                dummy=nexts
            return prev
        fast=head
        slow=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        slow=reverselist(slow)
        fast=head
        while fast and slow:
            if fast.val!=slow.val:
                return False
            slow=slow.next
            fast=fast.next
        if fast:
            fast=fast.next
        if slow:
            slow=slow.next
        
        if fast or slow:
            return False
        else:
            return True
        

        