# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        def reverses(root1):
            if not root1:
                return
            root1.left,root1.right=root1.right,root1.left
            reverses(root1.left)
            reverses(root1.right)
        reverses(root)
        return root
        