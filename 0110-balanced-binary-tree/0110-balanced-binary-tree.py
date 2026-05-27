# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        self.answer=True
        def search(roots,j):
            if not roots:
                return j
            l=search(roots.left,j+1)
            r=search(roots.right,j+1)
            if abs(r-l)>1:
                self.answer=False
            return max(r,l)
            
        search(root,0)

        return self.answer
        
        
        