# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        answer=[]
        size=0
        temp=head
        while temp:
            size+=1
            temp=temp.next
        window=size//k
        extra=size%k
        temp=head
        for i in range(k):
            temph=temp
            siz=window + (1 if i<extra else 0)
            for j in range(siz-1):
                if temp:
                    temp=temp.next
            if temp:
                nexts=temp.next
                temp.next=None
                temp=nexts
            answer.append(temph)
        return answer


        