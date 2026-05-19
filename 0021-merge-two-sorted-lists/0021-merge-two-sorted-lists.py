# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        def answer(answers,list1,list2):
            if not list1 and not list2:
                return 
            if not list1 and list2:
                answers.next=list2
                return
            if not list2 and list1:
                answers.next=list1
                return
            if list1.val>=list2.val:
                answers.next=list2
                list2=list2.next
            else:
                answers.next=list1
                list1=list1.next
            answer(answers.next,list1,list2)
        dummy=ListNode(1)
        answer(dummy,list1,list2)
        return dummy.next

        


        
        