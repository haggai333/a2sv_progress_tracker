# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.answer=0
        def find(roots,i):
            if not roots:
                return 0
            l=find(roots.left,i+1)
            r=find(roots.right,i+1)
            self.answer=max(self.answer,l+r)
            return 1+max(l,r)
        find(root,0)
        return self.answer

        