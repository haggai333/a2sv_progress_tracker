# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        temp=head
        prev=None
        if head:
            prev=head.next
        if temp and temp.next:
            nexts=temp.next.next
            head=temp.next
            head.next=temp
            temp.next=nexts
            prev=temp
        if temp:
            temp=temp.next
        while temp and temp.next:
            nexts=temp.next.next
            prev.next=temp.next
            prev.next.next=temp
            temp.next=nexts
            prev=temp
            temp=temp.next
            

        return head
        