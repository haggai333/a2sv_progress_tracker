# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        seen=set()
        while headA or headB:
            if headA:
                if headA in seen:
                    return headA
                else:
                    seen.add(headA)
                headA=headA.next
            if headB:
                if headB in seen:
                    return headB
                else:
                    seen.add(headB)
                headB=headB.next
        return None

        