# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        def answer(list1,list2):
            if not list1 and not list2:
                return None
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val>=list2.val:
                list2.next=answer(list1,list2.next)
                return list2
            else:
                list1.next=answer(list1.next,list2)
                return list1
            
        return answer(list1,list2)

        


        
        