# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        self.answer=None
        self.count=0
        def check(roots):
            if not roots or self.answer:
                return
            check(roots.left)
            self.count+=1
            if self.count==k:
                self.answer=roots.val
                self.count+=1
                return
            check(roots.right)
        check(root)
        return self.answer

        