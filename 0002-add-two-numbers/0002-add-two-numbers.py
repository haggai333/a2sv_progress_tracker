# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry=0
        answer=ListNode(0)
        temp=answer
        while l1 or l2 or carry!=0:
            x=0
            y=0
            if l1 :
                x=l1.val
            if l2:
                y=l2.val
            sum=x+y+carry
            carry=sum//10
            temp.next=ListNode(sum%10)
            temp=temp.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return answer.next




        