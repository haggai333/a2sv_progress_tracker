# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        self.maxdepth=0
        def searchdepth(roots,i):
            if roots==None:
                self.maxdepth=max(self.maxdepth,i)
                return
            searchdepth(roots.left,i+1)
            searchdepth(roots.right,i+1)
        searchdepth(root,0)
        answer=[]
        for i in range(self.maxdepth):
            answer.append([])
        def construct(roots,i):
            if not roots:
                return
            answer[i].append(roots.val)
            construct(roots.left,i+1)
            construct(roots.right,i+1)
        construct(root,0)
        return answer



        