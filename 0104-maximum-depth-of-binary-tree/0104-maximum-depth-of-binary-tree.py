# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.answer=0
        def search(heads,count):
            if heads==None:
                self.answer=max(self.answer,count)
                return
            search(heads.left,count+1)
            search(heads.right,count+1)
            
        search(root,0)
        return self.answer
        