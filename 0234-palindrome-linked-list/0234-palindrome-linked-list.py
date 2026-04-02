# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow=head
        fast=head
        prev=None
        count=0
        while fast:
            fast=fast.next
            count+=1
        fast=head
        
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        
        a=slow
        b=None
        while a:
                t=a.next
                a.next=b
                b=a
                a=t
        
        
        for i in range(count//2):
            if head.val!=b.val:
                return False
            head=head.next
            b=b.next
        return True


        
        

        