# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        start=head
        prev=None
        size=0
        while start:
            prev=start
            start=start.next
            size+=1
        if size<2:
            return head
        prev.next=head
        k=k%size
        c=0
        start=head
        while c<size-k-1:
            start=start.next
            c+=1
        answer=start.next
        start.next=None
        return answer

        