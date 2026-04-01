# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        a=set()
        count=0
        while head:
            if head in a:
                return True
            a.add(head)
            count+=1
            head=head.next
        return False
        
        