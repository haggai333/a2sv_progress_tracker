# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        def answer(temp,prev):
            if not temp:
                return prev
            nexts=temp.next
            temp.next=prev
            prev=temp
            return answer(nexts,prev)
        return answer(head,None)
        




        