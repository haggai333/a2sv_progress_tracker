# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head=ListNode(0)
        answer=head
        while list1 or list2:
            while list1 and list2:
                if list1.val<=list2.val:
                    answer.next=ListNode(list1.val)
                    answer=answer.next
                    list1=list1.next
                   
                else:
                    answer.next=ListNode(list2.val)
                    answer=answer.next
                    list2=list2.next
                    
            if list1:
                answer.next=ListNode(list1.val)
                answer=answer.next
                list1=list1.next
                
            if list2:
                answer.next=ListNode(list2.val)
                answer=answer.next
                list2=list2.next
                
        return head.next


        