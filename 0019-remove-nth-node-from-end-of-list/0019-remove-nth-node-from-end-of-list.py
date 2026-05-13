# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=ListNode(-1)
        temp.next=head
        dummy=temp
        prev=temp
        temp=temp.next

        count=0
        size=0
        fast=head
        while fast:
            size+=1
            fast=fast.next
        while temp:
            count+=1
            if size-count==n-1:
                prev.next=temp.next
                break
            prev=temp
            temp=temp.next
            
        return dummy.next
            
        