# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root,p, q):
        self.answer=None
        def check(roots):
            if not roots or self.answer:
                return
            if roots.val>=min(p.val,q.val) and roots.val<=max(p.val,q.val):
                self.answer=roots
                return
            if roots.val<min(p.val,q.val)and roots.val<max(p.val,q.val):
                check(roots.right)
                
            if roots.val>min(p.val,q.val) and roots.val>max(p.val,q.val) :
                check(roots.left)
                
                
        check(root)
        return self.answer


        
        