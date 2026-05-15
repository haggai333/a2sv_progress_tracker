# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if not head:
            return
        if not head.next:
            return
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                break
        if not fast:
            return
        if not fast.next:
            return
        fast=head
        while fast:
            if fast==slow:
                return fast
            fast=fast.next
            slow=slow.next
        
        