# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        self.answer=False
        def check(roots,roots2):
            if not roots and not roots2:
                return 1
            if not roots and roots2:
                return 0
            if roots and not roots2:
                return 0
            if roots.val==roots2.val:
                return check(roots.left,roots2.left)*check(roots.right,roots2.right)
            else:
                return 0
        def traverse(roots):
            if not roots or self.answer:
                return
            if roots.val==subRoot.val:
                p=check(roots,subRoot)==1
                if p==1:
                    self.answer=True
            if self.answer:
                return
            traverse(roots.left)
            traverse(roots.right)
        traverse(root)
        return self.answer
        