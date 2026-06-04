# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        self.answer=0
        def search(roots,maxi):
            if not roots:
                return
            if roots.val>=maxi:
                self.answer+=1
                maxi=roots.val
            search(roots.right,maxi)
            search(roots.left,maxi)
        search(root,-1*float('inf'))
        return self.answer

        