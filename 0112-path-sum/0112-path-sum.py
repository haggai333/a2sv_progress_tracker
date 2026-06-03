# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        self.answer=False
        def search(roots,sum):
            
            if not roots or self.answer:
                return
            sum+=roots.val
            if sum==targetSum and not roots.left and not roots.right:
                self.answer=True
                return
            
            search(roots.left,sum)
            search(roots.right,sum)
        search(root,0)
        return self.answer
        