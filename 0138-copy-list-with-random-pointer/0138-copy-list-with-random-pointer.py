"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        copy=Node(-1)
        a=head
        copys=copy
        while a:
            copys.next=Node(a.val)
            copys=copys.next
            a=a.next
        copy=copy.next
        copys=copy
        count={}
        a=head
        while a:
            count[a]=copys
            copys=copys.next
            a=a.next
        a=head
        copys=copy
        while a:
            if a.random:
                copys.random=count[a.random]
            copys=copys.next
            a=a.next


            
        return copy
            
        




        