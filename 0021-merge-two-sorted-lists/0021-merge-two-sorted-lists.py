# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode(-1)
        answer=dummy
        next1=None
        next2=None
        while list1 or list2:
            if list1 and list2:
                next1=list1.next
                next2=list2.next
                if list1.val<=list2.val:
                    dummy.next=list1
                    list1=next1
                else:
                    dummy.next=list2
                    list2=next2
                dummy=dummy.next
            if not list1 and list2:
                dummy.next=list2
                dummy=dummy.next
                list2=list2.next
            if not list2 and list1:
                dummy.next=list1
                dummy=dummy.next
                list1=list1.next
        return answer.next
        


        
        