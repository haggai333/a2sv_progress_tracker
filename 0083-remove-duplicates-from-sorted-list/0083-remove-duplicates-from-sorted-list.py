# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        a=head
        if not head:
            return head
        temp=head.next
        while temp:
            if temp.val==a.val:
                temp=temp.next
                continue
            if a.next!=temp:
                a.next=temp
            a=temp
            temp=temp.next
        a.next=None

        return head
        