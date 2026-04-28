# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer=[]

        def search(heads):
            if heads==None:
                return
            
            search(heads.left)
            
            search(heads.right)
            answer.append(heads.val)
            
        search(root)
        return answer

        