# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        def reverseList(head):
            prev=None
            current=head
            while current:
                tmp=current.next
                current.next=prev
                prev=current
                current=tmp
            return prev
        answer=float('inf')*-1
        temp=head
        fast=head
        prev=None
        while fast and fast.next:
            prev=temp
            temp=temp.next
            fast=fast.next.next
        prev.next=None
        temp=reverseList(temp)
        while temp and head:
            k=temp.val+head.val
            answer=max(k,answer)
            temp=temp.next
            head=head.next
        
        return answer
        