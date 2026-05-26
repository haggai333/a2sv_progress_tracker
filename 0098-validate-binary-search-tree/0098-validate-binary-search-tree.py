# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        self.answer=True
        def check(roots,l,r):
            if not roots:
                return 
            if roots.val<=l or roots.val>=r:
                self.answer=False
                return
            check(roots.right,max(l,roots.val),r)
            check(roots.left,l,min(r,roots.val))
        check(root,-1*float('inf'),float('inf'))
        return self.answer