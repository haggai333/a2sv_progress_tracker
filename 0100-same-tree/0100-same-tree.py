# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        tree1=[]
        tree2=[]
        def construct(head):
            if head==None:
                tree1.append(None)
                return 
            tree1.append(head.val)
            construct(head.left)
            construct(head.right)
        def constructs(head):
            if head==None:
                tree2.append(None)
                return
            tree2.append(head.val)
            constructs(head.left)
            
            constructs(head.right)
        construct(p)
        constructs(q)
        return tree1==tree2

            


        