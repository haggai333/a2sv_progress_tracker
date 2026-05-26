# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        answer=[]
        def construct(roots,i):
            if not roots:
                return
            if len(answer)<i+1:
                answer.append([])
            answer[i].append(roots.val)
            construct(roots.left,i+1)
            construct(roots.right,i+1)
        construct(root,0)
        return answer



        