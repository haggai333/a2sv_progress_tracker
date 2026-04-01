# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count=0
        current=0
        temp=head
        answer=head
        while temp:
            if current-count==n+1:
                answer=answer.next
                count+=1
            temp=temp.next
            current+=1
        a=answer.next
        
        if a and current>n:
            answer.next=a.next
        elif a and n==2:
            head=head.next

        else:
            head=a
        return head
        
        