# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        self.answer=0
        def searchdepth(roots,i):
            if roots==None:
                self.answer=max(self.answer,i)
                return
            searchdepth(roots.left,i+1)
            searchdepth(roots.right,i+1)
        searchdepth(root,0)
        return self.answer
        